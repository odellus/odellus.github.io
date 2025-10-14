---
date: "2025-09-27"
title: "Crystals"
---

# SearXNG setup

## Step 1 - Install SearXNG

Open a terminal in MacOS or Linux [if you are using Windows consider your life choices up to this point and download a real operating system please] and do the following


They have detailed instructions [elsewhere][] on how to do this but I am trying to keep this self-contained.
```bash
mkdir -p ~/some/path/for/searxng/searxng
cd ~/some/path/for/searxng
docker pull searxng/searxng
export PORT=8082
docker run --rm -d -p ${PORT}:8080 \
 -v "${PWD}/searxng:/etc/searxng" \
 -e "BASE_URL=http://localhost:$PORT/" \
 -e "INSTANCE_NAME=the-index" \
 searxng/searxng
```
after you run it the first time you will see it write a comprehensive `settings.yml` file. Inside that file you will need to make a change and add the following

```yaml
  # Where you see  this
  formats:
    - html
    - json # <- Add this line
```
and restart
```
docker contaienr ls
docker stop <container_id>
# redo steps above to rerun searxng with new settings and response format json
```

you can test it out by going to http://localhost:8082 in the browser or you can try it from the command line like so
```bash
curl "http://localhost:8082/search?q=some+search+query&format=json"
```

Outstanding! You should see how to programmatically access search now from your local command line, but let's take it to the next level.

## Search MCP
Step 1 is to install [uv from astral](https://astral.sh) if you haven't already with

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then let's make a directory for our MCP server with the following in a terminal
```bash
mkdir -p ~/some/path/to/search_mcp
cd ~/some/path/to/search_mcp
uv init .
uv venv
source .venv/bin/activate
uv add fastmcp
nano main.py
```

and put the following script in `main.py`

```python
from typing import Optional
from httpx import AsyncClient
from os import getenv

from pydantic import BaseModel, Field
from fastmcp import FastMCP

mcp = FastMCP(name="SearXNGTools")



@mcp.tool
async def web_search(query: str, limit: int = 5) -> str:
    """Search the internet.
    Arguments:
        query: str - Your search query for the search engine.
        limit: int = 5 - optional argument to control the number of results
    Example use:
       result: str = search(query="How to make key lime pie")
    """
    client = AsyncClient(base_url=str(getenv("SEARXNG_URL", "http://localhost:8082")))

    params: dict[str, str] = {"q": query, "format": "json"}

    response = await client.get("/search", params=params)
    response.raise_for_status()

    data = Response.model_validate_json(response.text)

    text = ""

    for index, infobox in enumerate(data.infoboxes):
        text += f"Infobox: {infobox.infobox}\n"
        text += f"ID: {infobox.id}\n"
        text += f"Content: {infobox.content}\n"
        text += "\n"

    if len(data.results) == 0:
        text += "No results found\n"

    for index, result in enumerate(data.results):
        text += f"Title: {result.title}\n"
        text += f"URL: {result.url}\n"
        text += f"Content: {result.content}\n"
        text += "\n"

        if index == limit - 1:
            break

    return str(text)


class SearchResult(BaseModel):
    url: str
    title: str
    content: str
    # thumbnail: Optional[str] = None
    # engine: str
    # parsed_url: list[str]
    # template: str
    # engines: list[str]
    # positions: list[int]
    # publishedDate: Optional[str] = None
    # score: float
    # category: str


class InfoboxUrl(BaseModel):
    title: str
    url: str


class Infobox(BaseModel):
    infobox: str
    id: str
    content: str
    # img_src: Optional[str] = None
    urls: list[InfoboxUrl]
    # attributes: list[str]
    # engine: str
    # engines: list[str]


class Response(BaseModel):
    query: str
    number_of_results: int
    results: list[SearchResult]
    # answers: list[str]
    # corrections: list[str]
    infoboxes: list[Infobox]
    # suggestions: list[str]
    # unresponsive_engines: list[str]


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

And now you've got the environmet and the script you need. If you host somewhere other than localhost:8082 then put SEARXNG_URL=<your_instance_url> in a `.env` file and modify to load_env and you'll be set.

## Add to zed or VS Code or Continue or Cursor
There's a pattern for setting up MCP servers in IDEs. I use [zed](https://zed.dev/docs/ai/mcp) so my configuration for `web_search` looks like the following in my `settings.json` though your editor may vary

```json
"some-mcp-server": {
      "source": "custom",
      "enabled": true,
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/Users/thomas.wood/src/smolagents-example",
        "/Users/thomas.wood/src/smolagents-example/search.py"
      ],
      "env": {}
    }
```

and then when you're asking your llm questions you can say "search the internet for this" and it _will_.
