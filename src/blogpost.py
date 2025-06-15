#!/usr/bin/env python3
import argparse
import json
import sys
import re
from yaml import safe_load
from pathlib import Path
import pandas as pd
from feedgen.feed import FeedGenerator
import unist as u

DEFAULTS = {"number": 10}

root = Path(__file__).parent.parent
journal_dir = root / "journal"

print(f"Looking for posts in: {journal_dir}", file=sys.stderr)

# Aggregate all posts from the markdown and ipynb files
posts = []
for ifile in journal_dir.rglob("*.md"):
    print(f"Found file: {ifile}", file=sys.stderr)
    if "drafts" in str(ifile):
        print(f"Skipping draft: {ifile}", file=sys.stderr)
        continue

    text = ifile.read_text()
    try:
        _, meta, content = text.split("---", 2)
    except Exception as e:
        print(f"Skipping file with error: {ifile} - {str(e)}", file=sys.stderr)
        continue

    # Load in YAML metadata
    meta = safe_load(meta)
    if meta is None:
        print(f"Skipping file with invalid YAML: {ifile}", file=sys.stderr)
        continue
    
    # Construct the path relative to journal directory
    rel_path = ifile.relative_to(journal_dir)
    meta["path"] = rel_path.with_suffix("")
    print(f"Processed post: {meta['path']}", file=sys.stderr)
    
    if "title" not in meta:
        lines = text.splitlines()
        for ii in lines:
            if ii.strip().startswith("#"):
                meta["title"] = ii.replace("#", "").strip()
                break
    
    # Summarize content
    skip_lines = ["#", "--", "%", "++"]
    content = "\n".join(ii for ii in content.splitlines() if not any(ii.startswith(char) for char in skip_lines))
    N_WORDS = 50
    words = " ".join(content.split(" ")[:N_WORDS])
    if not "author" in meta or not meta["author"]:
        meta["author"] = "Thomas Wood"
    meta["content"] = meta.get("description", words)
    posts.append(meta)

posts = pd.DataFrame(posts)
posts["date"] = pd.to_datetime(posts["date"]).dt.tz_localize("US/Pacific")
posts = posts.dropna(subset=["date"])
posts = posts.sort_values("date", ascending=False)

plugin = {
    "name": "Blog Post list",
    "directives": [
        {
            "name": "postlist",
            "doc": "An example directive for showing a nice random image at a custom size.",
            "alias": ["bloglist"],
            "arg": {},
            "options": {
                "number": {
                    "type": "int",
                    "doc": "The number of posts to include",
                }
            },
        }
    ],
    "transforms": [
        {
            "name": "parse-blog-math",
            "doc": "Transform to parse math expressions in blog post cards",
            "stage": "document"
        }
    ],
}

children = []
for ix, irow in posts.iterrows():
    # Convert path to ABlog's expected format
    path_parts = str(irow['path']).split('/')
    if len(path_parts) == 3:  # year/month/filename
        year, month, filename = path_parts
        # Convert to lowercase for consistency
        month = month.lower()
        # Remove the date prefix if it exists
        if filename.startswith(year[-2:] + month[:3]):
            filename = filename[len(year[-2:] + month[:3]):]
        url = f"/journal/{year}/{month}/{filename}"
    else:
        url = f"/journal/{irow['path']}"
        
    children.append(
        {
          "type": "card",
          "url": url,
          "children": [
            {
              "type": "cardTitle",
              "children": [u.text(irow["title"])]
            },
            {
              "type": "paragraph",
              "children": [
                {
                  "type": "text",
                  "value": irow['content']
                }
              ],
              "data": {
                "needsMathParsing": True
              }
            },
            {
              "type": "footer",
              "children": [
                u.strong([u.text("Date: ")]), u.text(f"{irow['date']:%B %d, %Y} | "),
                u.strong([u.text("Author: ")]), u.text(f"{irow['author']}"),
              ]
            },
          ]
        }
    )


def find_all_by_type(node: dict, type_: str):
    """Simple node visitor that matches a particular node type"""
    if node["type"] == type_:
        yield node
    if "children" not in node:
        return
    for next_node in node["children"]:
        yield from find_all_by_type(next_node, type_)


def parse_math_expressions(text_value):
    """Parse math expressions and create proper AST nodes"""
    nodes = []
    
    # Pattern for inline math: $...$
    math_pattern = r'\$([^$\n]+)\$'
    last_end = 0
    
    for match in re.finditer(math_pattern, text_value):
        # Add text before math
        if match.start() > last_end:
            before_text = text_value[last_end:match.start()]
            if before_text:
                nodes.append({
                    "type": "text",
                    "value": before_text
                })
        
        # Try the exact structure that MyST uses for inline math
        math_content = match.group(1)
        nodes.append({
            "type": "inlineMath",
            "value": math_content,
            "position": {
                "start": {"line": 1, "column": match.start() + 1},
                "end": {"line": 1, "column": match.end() + 1}
            }
        })
        
        last_end = match.end()
    
    # Add remaining text
    if last_end < len(text_value):
        remaining_text = text_value[last_end:]
        if remaining_text:
            nodes.append({
                "type": "text", 
                "value": remaining_text
            })
    
    return nodes if nodes else [{"type": "text", "value": text_value}]


def declare_result(content):
    """Declare result as JSON to stdout"""
    json.dump(content, sys.stdout, indent=2)
    raise SystemExit(0)


def run_transform(name, data):
    """Execute a transform with the given name and data"""
    assert name == "parse-blog-math"
    
    # Find paragraphs that need math parsing
    for para_node in find_all_by_type(data, "paragraph"):
        if para_node.get("data", {}).get("needsMathParsing"):
            new_children = []
            
            for child in para_node.get("children", []):
                if child["type"] == "text":
                    # Parse math expressions
                    parsed_nodes = parse_math_expressions(child["value"])
                    new_children.extend(parsed_nodes)
                else:
                    new_children.append(child)
            
            # Update the paragraph
            para_node["children"] = new_children
            para_node["data"] = {"hasMath": True}
    
    return data


def run_directive(name, data):
    """Execute a directive with the given name and data"""
    assert name == "postlist"
    opts = data["node"].get("options", {})
    number = int(opts.get("number", DEFAULTS["number"]))
    output = children[:number]
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        result = run_directive(args.directive, data)
        declare_result(result)
    elif args.transform:
        data = json.load(sys.stdin)
        declare_result(run_transform(args.transform, data))
    elif args.role:
        raise NotImplementedError
    else:
        # If no arguments, just output the plugin configuration
        declare_result(plugin)
