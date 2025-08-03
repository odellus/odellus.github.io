---
date: "2025-08-03"
title: "plan-execute"
---

:::{tip} My version of plan-execute
This comes from [plan-execute][plan-execute] tutorial on langgraph's doc site. I have put it in its [own repo][my-plan-execute] too 
:::

# Imports
First we have a bunch of imports

```python
from pydantic import BaseModel, Field
import operator
from typing import Annotated, List, Tuple, Union, Literal
from typing_extensions import TypedDict
import asyncio

from langchain_community.tools.searx_search.tool import SearxSearchResults
from langchain_community.utilities import SearxSearchWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

from dotenv import load_dotenv
from phoenix.otel import register


# DO THIS BEFORE TRYING TO SET UP TRACER_PROVIDER
load_dotenv()

# configure the Phoenix tracer AFTER CALLING load_dotenv()
tracer_provider = register(
  project_name="plan-execute", # Default is 'default'
  auto_instrument=True # Auto-instrument your app based on installed OI dependencies
)
```
Now our agent is registered with Arize Phoenix. I freaking love arize phoenix.


# Models

We define the classes we need next. They keep it pretty light without many `Field`s 
```python

class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    response: str

class Plan(BaseModel):
    """Plan to follow in future"""

    steps: List[str] = Field(
        description="different steps to follow, should be in sorted order"
    )

class Response(BaseModel):
    """Response to user."""
    response: str = Field(
        description="The final response to the user's query."
        "Only use when you have the answer.",
    )


class Act(BaseModel):
    """Action to perform."""
    action: Union[Response, Plan] = Field(
        description="Action to perform. If you want to respond to user because you have the answer, use Response. "
        "If you need to further use tools to get the answer, use Plan."
    )
```


# Helper Functions and Tools
Define the planner, replanner, and execute agent here so we can use them in the nodes of our graph.
```python
def get_planner(llm):
    planner_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """For the given objective, come up with a simple step by step plan. \
    This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
    The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.""",
            ),
            ("placeholder", "{messages}"),
        ]
    )
    planner = planner_prompt | llm.with_structured_output(Plan)
    return planner


def get_replanner(llm):
    replanner_prompt = ChatPromptTemplate.from_template(
    """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Your objective was this:
{input}

Your original plan was this:
{plan}

You have currently done the follow steps:
{past_steps}

Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.
Never respond with steps: []. Instead respond with Response action.
"""

    )

    replanner = replanner_prompt | llm.with_structured_output(Act)
    return replanner


def get_searxng_tool(num_results=3):
    wrapper = SearxSearchWrapper(searx_host="http://localhost:8082")
    return SearxSearchResults(wrapper=wrapper, num_results=num_results)
    

def get_llm(model):
    return ChatOpenAI(
        model=model,
        base_url='http://localhost:11434/v1', 
        api_key='ollama',
    )

def create_execute_agent(model='qwen3:latest', num_results=5):
    llm = get_llm(model=model)
    tools = [get_searxng_tool(num_results=num_results)]
    prompt = "You are a helpful assistant."
    return create_react_agent(llm, tools, prompt=prompt)

# Our helper functions return objects
llm = get_llm("qwen3:latest")
planner = get_planner(llm)
replanner = get_replanner(llm)
agent_executor = create_execute_agent(model='qwen3:latest', num_results=3)
```
# Nodes

We set up nodes that perform actions on the graph state here.
:::{tip} Documentation yields better code
I just changed this in the journal while I was writing it up to use Command instead of just `return {**update}`.
:::
```python
async def execute_step(state: PlanExecute):
    plan = state["plan"]
    plan_str = "\n".join(f"{i + 1}. {step}" for i, step in enumerate(plan))
    if len(plan) < 1:
        task = "Answer the user with Response action."
    else:
        task = plan[0]
    task_formatted = f"""For the following plan:
{plan_str}\n\nYou are tasked with executing step {1}, {task}."""
    agent_response = await agent_executor.ainvoke(
        {"messages": [("user", task_formatted)]}
    )
    return Command(
        update={"past_steps": [(task, agent_response["messages"][-1].content)]},
        goto="replan_step",
    )


async def plan_step(state: PlanExecute):
    plan = await planner.ainvoke({"messages": [("user", state["input"])]})
    return Command(update={"plan": plan.steps}, goto="execute_step")


async def replan_step(state: PlanExecute):
    output = await replanner.ainvoke(state)
    if isinstance(output.action, Response):
        return Command(update={"response": output.action.response}, goto=END)
    else:
        return Command(update={"plan": output.action.steps}, goto="execute_step")

```
# Edges
This tutorial seems to be a bit older so they aren't using `Command` the way I like to do these days. Might revisit this later to see if there's a way to re-do the architecture and set it up for HITL with `interrupt` and `Command`. But for now we set it up the same way they do in the tutorial. The `should_end` is how they used to do Command before they had Command.

:::{important} Documenting in motion
I wrote the above comment earlier. I went ahead and did it.
:::
```python
def get_graph():

    workflow = StateGraph(PlanExecute)

    # Add the plan node
    workflow.add_node("plan_step", plan_step)

    # Add the execution step
    workflow.add_node("execute_step", execute_step)

    # Add a replan node
    workflow.add_node("replan_step", replan_step)

    workflow.add_edge(START, "plan_step")

    # Finally, we compile it!
    # This compiles it into a LangChain Runnable,
    # meaning you can use it as you would any other runnable
    app = workflow.compile()
    return app
```
# Run
```python
async def main():
    app = get_graph()
    config = {"recursion_limit": 50}
    inputs = {"input": "what is the hometown of the mens 2024 Australia open winner?"}
    async for event in app.astream(inputs, config=config):
        for k, v in event.items():
            if k != "__end__":
                print(v)


if __name__ == "__main__":
    asyncio.run(main())

```
# Response
```
(plan-execute) (base) thomas@nunya-216:~/src/atlas_agent/plan-execute$ uv run main.py
🔭 OpenTelemetry Tracing Details 🔭
|  Phoenix Project: plan-execute
|  Span Processor: SimpleSpanProcessor
|  Collector Endpoint: localhost:4317
|  Transport: gRPC
|  Transport Headers: {'authorization': '****'}
|  
|  Using a default SpanProcessor. `add_span_processor` will overwrite this default.
|  
|  ⚠️ WARNING: It is strongly advised to use a BatchSpanProcessor in production environments.
|  
|  `register` has set this TracerProvider as the global OpenTelemetry default.
|  To disable this behavior, call `register` with `set_global_tracer_provider=False`.

{'plan': ["Identify the winner of the Men's 2024 Australia Open.", 'Determine the hometown of the identified winner.', 'Verify the information to ensure accuracy.']}
{'past_steps': [("Identify the winner of the Men's 2024 Australia Open.", "<think>\nOkay, let me process the search results to find the winner of the Men's 2024 Australia Open. The first result seems to be about the honour roll page, which might not have the latest info. The second snippet from BBC Sport mentions Jannik Sinner beating Daniil Medvedev in the final. The third result from the Australian Open's official site also states that Jannik Sinner won the 2024 men's singles title. Both sources agree he's the winner. So, the answer is Jannik Sinner. Now, I should verify if there's any conflicting info, but both top results point to him. I'll confirm that and proceed to the next step.\n</think>\n\nThe winner of the Men's 2024 Australia Open is **Jannik Sinner**. He defeated Daniil Medvedev in the final to claim the title. \n\nNext step: Determine Jannik Sinner's hometown.")]}
{'plan': ['Determine the hometown of Jannik Sinner.']}
{'past_steps': [('Determine the hometown of Jannik Sinner.', '<think>\nOkay, let me process this. The user asked for Jannik Sinner\'s hometown. Looking at the search results, the first snippet mentions he was born in Innichen, South Tyrol, Italy. The third snippet also says he was born in San Candido, Italy. Wait, are Innichen and San Candido the same place? Maybe they are different towns in the same region. Let me check the details.\n\nThe first result says his hometown is Sexten in the Dolomites, where his father worked. Wait, the snippet says "the family hometown, where his father worked as a chef..." So the family moved to Sexten. But his birthplace is Innichen. The third snippet lists San Candido as his birthplace. Hmm, there might be some confusion here. Let me verify.\n\nWait, maybe San Candido and Innichen are both in South Tyrol. Let me check. San Candido is a town in South Tyrol, and Innichen is another town nearby. Wait, actually, Innichen is a town in the South Tyrol region, and San Candido is also in the same area. Maybe the sources are referring to different aspects: birthplace vs. hometown. The first result says he was born in Innichen but grew up in Sexten. The third snippet says born in San Candido. This could be conflicting information. Wait, perhaps there\'s a mistake in the third snippet. Let me check the first result again. The first snippet says "born 16 August 2001 to Hanspeter and Siglinde Sinner in Innichen, in the Northern Italian province of South Tyrol. His mother tongue is German. He grew up in the town of Sexten in the Dolom, the family hometown..." So his birthplace is Innichen, but his family hometown is Sexten. The third snippet might have an error, stating San Candido. Alternatively, maybe San Candido is another name for Innichen? Wait, San Candido is a different town. Wait, perhaps the third snippet is incorrect. Let me check the first result again. The first result\'s snippet says he was born in Innichen, South Tyrol. The third snippet says "born August 16, 2001, San Candido, Italy". So there\'s a discrepancy here. Which one is correct? Maybe I need to cross-verify. Let me think. The first result is from Wikipedia, which is a reliable source. The third is from Britannica. If the first result is accurate, then the correct hometown is Sexten, but birthplace is Innichen. However, the user asked for hometown, not birthplace. So the answer would be Sexten. But the first snippet says "grew up in the town of Sexten in the Dolomites, the family hometown". So the answer is Sexten. However, the third snippet might have an error. But the user might be looking for the birthplace. Wait, the user asked for hometown, so the correct answer is Sexten. But I need to confirm. Let me check the first result again. The first snippet says "born in Innichen... grew up in Sexten... family hometown". Therefore, the hometown is Sexten. The third snippet might have an error. So the answer is Sexten, Italy.\n</think>\n\nThe hometown of Jannik Sinner is **Sexten** (also spelled *Sexten* or *Sexten in the Dolomites*), located in the South Tyrol region of northern Italy. While he was born in **Innichen** (also in South Tyrol), his family grew up in Sexten, which is considered his hometown.')]}
{'response': "The hometown of the men's 2024 Australia Open winner, Jannik Sinner, is **Sexten** (in the Dolomites, South Tyrol, northern Italy)."}
```

# Holy cow that's a lotta steps

:::{figure} ../images/plan-execute-phoenix-trace.png
You can really drill down into it in phoenix, which is pretty much valgrind for agents.
:::
This is cool! Multi-agent Sunday. There was something else I really wanted to do today. Oh yeah read a paper with a bunch of math in it. I mean I sort of did some math [yesterday][aug-02] with the $NewtonSchulz5$ stuff even though that was mostly kimi k2 tbh. 

---
Yeah I love being able to cross reference my equations like Eqn. [](#ns-scalar) 


[my-plan-execute]: https://github.com/odellus/plan-execute-langgraph
[plan-execute]: https://langchain-ai.lang.chat/langgraph/tutorials/plan-and-execute/plan-and-execute/
[aug-02]: ./aug02