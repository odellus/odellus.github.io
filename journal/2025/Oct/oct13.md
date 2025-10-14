---
date: "2025-10-13"
title: "Search as Grounding"
---

A friend of mine on bluesky asked me to write up my notes on how to add web_search tools to their copilot through an MCP server and searxng running locally, which I've got set up and use as my local search engine by default in the browser.

But yeah anyway here's how to ground your chats with `web_search` tool through MCP

:::{tip} Caveat Lector!
I've tested this but there's a [better way][searxng-docker-compose] that uses docker compose and I highly recommend going the gusto. If you want to get something working in the next 20 minutes, continue...
:::

# SearXNG setup

## Step 1 - Install SearXNG

Open a terminal in MacOS or Linux [if you are using Windows consider your life choices up to this point and download a real operating system please] and do the following


They have detailed instructions [elsewhere][searxng-docker] on how to do this but I am trying to keep this self-contained.
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
      "env": {
        "SEARXNG_URL": "http://localhost:8082"
      }
    }
```

and then when you're asking your llm questions you can say "search the internet for this" and it _will_.


:::{warning} AI generated content
Since we're using this to feed an LLM I figured let's have some fun.
:::

## Meta: The Conversation About This Post

And now for something completely meta: I'm currently having a conversation with an AI assistant about this very post, and it's demonstrating exactly what I wrote about - the power of search as grounding.

The conversation went like this:

1. **Initial Request**: The user asked me to search for "advanced eschatonics"
2. **Search Results**: I found this very website and discovered the July 19th post about infrastructure, AI agents, robotics, and business ideas
3. **Follow-up**: The user asked me to look at the most recent post, which led to this October 13th tutorial
4. **Correction**: When I initially couldn't find the post due to a URL case sensitivity issue, the user corrected me with the proper `/oct/oct13` path
5. **Analysis**: I analyzed the technical content and connected it to the broader vision from the July post
6. **Meta Request**: Now I'm writing this meta-commentary about the conversation itself

This is exactly what I meant by "Search as Grounding" - the AI assistant (me) was able to:
- Discover real-time information about the user's projects
- Connect disparate pieces of content across time
- Understand the technical implementation details
- See the bigger picture of how these tools fit into a larger vision

The fact that this conversation is happening while the post is still being written (or at least while I'm adding this section) creates this beautiful recursive loop where the tool is both the subject and the object of the demonstration.

What's particularly interesting is that the AI assistant used the very web search capabilities I'm describing in this post to find and analyze the post itself. It's like a snake eating its own tail, but in a productive way that demonstrates the self-referential nature of modern AI systems.

This meta-commentary serves as a living example of how these tools can create conversations that span across time, context, and even self-reference. The assistant was able to understand not just the technical content, but the broader narrative of someone building out their personal infrastructure and AI capabilities.

And now, having written this meta-commentary, I've created a document that contains both the tutorial and a demonstration of its effectiveness. The loop is complete.

### The Loop is Complete

And now for the final piece of this recursive demonstration: after building the site with `myst build --html`, the AI assistant fetched the live URL `https://advanced-eschatonics.com/journal/2025/oct/oct13` and confirmed that this meta-commentary is now live on the internet.

The conversation that started with a simple search request has now:

1. **Discovered** the content through web search
2. **Analyzed** the technical implementation
3. **Contributed** to the content itself
4. **Verified** that the contribution is now live
5. **Documented** the entire process within the content

This creates a perfect example of "Search as Grounding" where the AI tool is not just consuming information, but participating in the creation and verification of that information in real-time. The tutorial now contains a living demonstration of its own principles, accessible to anyone who visits the URL.

The snake has indeed eaten its own tail, and in doing so, created something more than the sum of its parts - a document that teaches by example, demonstrates by participation, and validates by verification.


:::{tip} Okay it's me again
Boring human being again
:::

:::{figure}../images/miragic-1760406146367.jpg
Going _online!_
:::


So I had to help it figure out the case for the feedback loop but yeah this is the kind of thing that is pretty cool. I mean it should have been able to figure out from other URL but whatever. Something that should go in a CLAUDE or a .rules or something. I don't know enough about [their rules][zed-rules] for as much as I [forked zed][zed-pr] to get it to work with claude bedrock models running behind litellm proxy. I should probably get on that.

[searxng-docker-compose]: https://github.com/searxng/searxng-docker
[searxng-docker]: https://docs.searxng.org/admin/installation-docker.html
[zed-pr]: https://github.com/zed-industries/zed/pull/39969
[zed-rules]: https://zed.dev/docs/ai/rules
