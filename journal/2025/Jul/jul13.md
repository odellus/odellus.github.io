---
date: "2025-07-13"
title: "URDF and trae-agent"
---

# Sim2Real

I don't know. What did I do this week? Feels strange like the sixth was more than five days ago.

The Sim2Real failed because the Real2Sim step wasn't accurate enough.

I started putting the meshes that make up the robot base and camera mounts together with the mesh for the base of the robot from maniskill and they're on completely different scales. So I've got to figure out how I'm going to shrink the mount mesh down to size to align it with the base. Then I have the position and orientation of the camera right there in the URDF. I can make some cylinder to model the webcam it's fine.

I need to be doing this after work. I need to be investigating different photogrammetry techniques and ways to find the kinematic parameters of generic objects. I need to be learning more about semantic segmentation and the state of the art of image -> 3D mesh models. Depth estimation? Shape completion++. I don't know. There's so much to learn. [AutoURDF][auto-urdf] seems like the perfect place to start.

And there's [Infinigen-Sim][infinigen].


Connecting Blender/CAD with the real world and back again is exactly the idea. Matter hacking.

Digital twins.


# `trae-agent`

So they've been busy on trae agent since last week. Now they've got it set up to where you can use OpenRouter so I created an account on OpenRouter for my trae-agent use.

I want to put it into continue. Or make a new visual studio extension for it. I mean it's basically amp or claude code.

I haven't tried with any more sophisticated examples. Or anywhere outside the trae-agent directory. Not sure how to get it to load in the correct configuration when I call `trae-cli` directly from some directory other the agent's root repo. Guess I can solve this with simple alias to the trae-cli with some default config path or something. 

Yeah that worked. I can also just do whatever I need to do with cloning and setup before passing in the path with `-w` to the cli. That's how you solve that if you don't want to run with 

```bash
/path/to/trae-agent/.venv/bin/trae-cli run \
    --config-file /path/to/trae-agent/trae_config.json \
    -w /path/to/root/of/moose \
    -p openrouter \
    "create a minimal working example of a multiphysics simulation for neutron diffusion and heat with the MOOSE simulation package in the root directory" 
```


I ended up spending $0.07 on openrouter and I saw how they were directing my backend calls across several different providers and it made me wonder if there's any way to do it that way and use prefix caching because I doubt it. Seeing these conversations extend in phoenix knowing I'm not only paying for each token again but suffering the latency of not having it warm in memory was making me wish I had that GX-10 they keep saying is supposed to come out this summer. 

I assume it is going to come out around the same time as the Nvidia Spark DGX. I looked into it and they only have one ethernet port. I don't know what kind of malarkey you.com was serving me the other day because they say they only have one ethernet port. So I need a router. The port looks like a normal ass port too not something you can plug some fancy cable that costs $200 into. Have to hold off on making any big plans until I have more first hand information.

I ended up just plugging in the base url of fireworks and my fireworks API key into the openrouter configuration and it works fine. I was deep into fixing the issue with the very initial release and I had it all figured out how I could get it working then I checked the github and they've got not one but two (minimum) new types of provider, ollama and openrouter, that are basically just the openai chat completions SDK as opposed to the Response API they initially released with. So yeah. LOL.

With more sophisticated sets of instructions/tasks it fails because they use the name of the task in creating the filename and there are limits to how long your filename can be.

:::{important} Updates
This needs to be a VS Code Extension!
:::

But it does sort of beg the question of what's so special about trae-agent. I mean continue can run code and access MCP servers. Also why isn't trae-agent an MCP server? It seems to be a very lightweight collection of tools in a trench coat. I am now reading the code instead of talking shit.

## Actual code

```python
class Agent(ABC):
    """Base class for LLM-based agents."""

    def __init__(self, config: Config | None = None, llm_client: LLMClient | None = None):
        """Initialize the agent.

        Args:
            config: Configuration object containing model parameters and other settings.
                   Required if llm_client is not provided.
            llm_client: Optional pre-configured LLMClient instance.
                       If provided, it will be used instead of creating a new one from config.
        """
        if llm_client is None:
            if config is None:
                raise ValueError("Either config or llm_client must be provided")
            self._llm_client = LLMClient(
                config.default_provider,
                config.model_providers[config.default_provider],
                config.max_steps,
            )
            self._model_parameters = config.model_providers[config.default_provider]
            self._max_steps = config.max_steps
        else:
            self._llm_client = llm_client
            self._model_parameters = llm_client.model_parameters
            self._max_steps = llm_client.max_steps

        self._initial_messages: list[LLMMessage] = []
        self._task: str = ""
        self._tools: list[Tool] = []
        self._tool_caller: ToolExecutor = ToolExecutor([])
        self._cli_console: CLIConsole | None = None

        # Trajectory recorder
        self._trajectory_recorder: TrajectoryRecorder | None = None

        # CKG tool-specific: clear the older CKG databases
        clear_older_ckg()
```

Which is all pretty clear honestly. What's a `ToolExecutor`? Well I checked it out. Here's what it is:

```python
class ToolExecutor:
    """Tool executor that manages tool execution."""

    def __init__(self, tools: list[Tool]):
        self._tools = tools
        self._tool_map: dict[str, Tool] | None = None

    @property
    def tools(self) -> dict[str, Tool]:
        if self._tool_map is None:
            self._tool_map = {tool.name: tool for tool in self._tools}
        return self._tool_map

    async def execute_tool_call(self, tool_call: ToolCall) -> ToolResult:
        """Execute a tool call."""
        if tool_call.name not in self.tools:
            return ToolResult(
                name=tool_call.name,
                success=False,
                error=f"Tool '{tool_call.name}' not found. Available tools: {list(self.tools.keys())}",
                call_id=tool_call.call_id,
                id=tool_call.id,
            )

        tool = self.tools[tool_call.name]

        try:
            tool_exec_result = await tool.execute(tool_call.arguments)
            return ToolResult(
                name=tool_call.name,
                success=tool_exec_result.error_code == 0,
                result=tool_exec_result.output,
                error=tool_exec_result.error,
                call_id=tool_call.call_id,
                id=tool_call.id,
            )
        except Exception as e:
            return ToolResult(
                name=tool_call.name,
                success=False,
                error=f"Error executing tool '{tool_call.name}': {str(e)}",
                call_id=tool_call.call_id,
                id=tool_call.id,
            )

    async def parallel_tool_call(self, tool_calls: list[ToolCall]) -> list[ToolResult]:
        """Execute tool calls in parallel"""
        return await asyncio.gather(*[self.execute_tool_call(call) for call in tool_calls])

    async def sequential_tool_call(self, tool_calls: list[ToolCall]) -> list[ToolResult]:
        """Execute tool calls in sequential"""
        return [await self.execute_tool_call(call) for call in tool_calls]
```


Which now begs the question what is one of these `Tool`s? Now we're getting to the meat of the `trae-agent` architecture. Here's an example of their [`BashTool`][bash-tool-trae]

```python
class BashTool(Tool):
    """
    A tool that allows the agent to run bash commands.
    The tool parameters are defined by Anthropic and are not editable.
    """

    def __init__(self, model_provider: str | None = None):
        super().__init__(model_provider)
        self._session: _BashSession | None = None

    @override
    def get_model_provider(self) -> str | None:
        return self._model_provider

    @override
    def get_name(self) -> str:
        return "bash"

    @override
    def get_description(self) -> str:
        return """Run commands in a bash shell
* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.
* You have access to a mirror of common linux and python packages via apt and pip.
* State is persistent across command calls and discussions with the user.
* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.
* Please avoid commands that may produce a very large amount of output.
* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.
"""

    @override
    def get_parameters(self) -> list[ToolParameter]:
        # For OpenAI models, all parameters must be required=True
        # For other providers, optional parameters can have required=False
        restart_required = self.model_provider == "openai"

        return [
            ToolParameter(
                name="command",
                type="string",
                description="The bash command to run.",
                required=True,
            ),
            ToolParameter(
                name="restart",
                type="boolean",
                description="Set to true to restart the bash session.",
                required=restart_required,
            ),
        ]

    @override
    async def execute(self, arguments: ToolCallArguments) -> ToolExecResult:
        if arguments.get("restart"):
            if self._session:
                self._session.stop()
            self._session = _BashSession()
            await self._session.start()

            return ToolExecResult(output="tool has been restarted.")

        if self._session is None:
            try:
                self._session = _BashSession()
                await self._session.start()
            except Exception as e:
                return ToolExecResult(error=f"Error starting bash session: {e}", error_code=-1)

        command = str(arguments["command"]) if "command" in arguments else None
        if command is None:
            return ToolExecResult(
                error=f"No command provided for the {self.get_name()} tool",
                error_code=-1,
            )
        try:
            return await self._session.run(command)
        except Exception as e:
            return ToolExecResult(error=f"Error running bash command: {e}", error_code=-1)

```

And that's how you let an LLM loose running code on your machine. There are other tools it has to use, but it probably needs more, or at least a tool-like interface to interact with another agent with its own tools devoted to search or something like that. There's [A2A][a2a-project] but I don't know how much it's being adopted. I mean bytedance decided to build their own coding agent around four (now five) tool calls instead of just making this an MCP and plugging it into a standard react agent from langgraph.


:::{note} TO DO
Compare this versus making these tools into a MCP that you can plug into a prebuilt react agent from langgraph.
:::


Okay I'm really at the heart of `trae-agent` now. Fuck I hate how much I sound like an LLM lol. Anyway I am continuing to read [`trae-agent/agent/base.py`][base-agent-trae].

### `execute_task`

```python
# Part of the same class Agent(ABC):
async def execute_task(self) -> AgentExecution:
        """Execute a task using the agent."""
        import time

        start_time = time.time()

        execution = AgentExecution(task=self._task, steps=[])

        step: AgentStep | None = None

        try:
            messages = self._initial_messages
            step_number = 1

            while step_number <= self._max_steps:
                step = AgentStep(step_number=step_number, state=AgentState.THINKING)

                try:
                    step.state = AgentState.THINKING
                    # Display thinking state
                    self._update_cli_console(step)

                    # Get LLM response
                    llm_response = self._llm_client.chat(
                        messages, self._model_parameters, self._tools
                    )
                    step.llm_response = llm_response

                    # Display step with LLM response
                    self._update_cli_console(step)

                    # Update token usage
                    self._update_llm_usage(llm_response, execution)

                    if self.llm_indicates_task_completed(llm_response):
                        if self._is_task_completed(llm_response):
                            self._llm_complete_response_task_handler(
                                llm_response, step, execution, messages
                            )
                            break
                        else:
                            step.state = AgentState.THINKING
                            messages = [
                                LLMMessage(role="user", content=self.task_incomplete_message())
                            ]
                    else:
                        # Check if the response contains a tool call
                        tool_calls = llm_response.tool_calls
                        messages = await self._tool_call_handler(tool_calls, step)

                    # Record agent step
                    self._record_handler(step, messages)
                    self._update_cli_console(step)

                    execution.steps.append(step)
                    step_number += 1

                except Exception as e:
                    step.state = AgentState.ERROR
                    step.error = str(e)

                    # Display error
                    self._update_cli_console(step)
                    # Record agent step
                    self._record_handler(step, messages)
                    self._update_cli_console(step)

                    execution.steps.append(step)
                    break

            if step_number > self._max_steps and not execution.success:
                execution.final_result = "Task execution exceeded maximum steps without completion."

        except Exception as e:
            execution.final_result = f"Agent execution failed: {str(e)}"

        execution.execution_time = time.time() - start_time

        # Display final summary
        if step:
            self._update_cli_console(step)

        return execution
```

### Let's break that down step-by-step
Okay so that's how it executes a task. What does it do?

- Sends a message to the llm with the available tools and the messages
```python

                    # Get LLM response
                    llm_response = self._llm_client.chat(
                        messages, self._model_parameters, self._tools
                    )
                    step.llm_response = llm_response

```
- Checks to see if the LLM says the task is completed, then checks if the task is actually completed (not implemented yet actually lol)
```python

                    if self.llm_indicates_task_completed(llm_response):
                        if self._is_task_completed(llm_response):
                            self._llm_complete_response_task_handler(
                                llm_response, step, execution, messages
                            )
                            break
                        else:
                            step.state = AgentState.THINKING
                            messages = [
                                LLMMessage(role="user", content=self.task_incomplete_message())
                            ]
```

- If the task is not complete, it handles the tool calls
```python
                    else:
                        # Check if the response contains a tool call
                        tool_calls = llm_response.tool_calls
                        messages = await self._tool_call_handler(tool_calls, step)
```

### Tool calls
Which brings us to the last part of the trae-agent base class, which is really interesting

```python
    async def _tool_call_handler(
        self, tool_calls: list[ToolCall] | None, step: AgentStep
    ) -> list[LLMMessage]:
        messages: list[LLMMessage] = []
        if not tool_calls or len(tool_calls) <= 0:
            messages = [
                LLMMessage(
                    role="user",
                    content="It seems that you have not completed the task.",
                )
            ]
            return messages

        step.state = AgentState.CALLING_TOOL
        step.tool_calls = tool_calls
        self._update_cli_console(step)

        if self.model_parameters.parallel_tool_calls:
            tool_results = await self._tool_caller.parallel_tool_call(tool_calls)
        else:
            tool_results = await self._tool_caller.sequential_tool_call(tool_calls)
        step.tool_results = tool_results
        self._update_cli_console(step)
        for tool_result in tool_results:
            # Add tool result to conversation
            message = LLMMessage(role="user", tool_result=tool_result)
            messages.append(message)

        reflection = self.reflect_on_result(tool_results)
        if reflection:
            step.state = AgentState.REFLECTING
            step.reflection = reflection

            # Display reflection
            self._update_cli_console(step)

            messages.append(LLMMessage(role="assistant", content=reflection))

        return messages
```

Here's the `reflect_on_results` function
```python
    def reflect_on_result(self, tool_results: list[ToolResult]) -> str | None:
        """Reflect on tool execution result. Override for custom reflection logic."""
        if len(tool_results) == 0:
            return None

        reflection = "\n".join(
            f"The tool execution failed with error: {tool_result.error}. Consider trying a different approach or fixing the parameters."
            for tool_result in tool_results
            if not tool_result.success
        )

        return reflection
```

When the tool calls error out it passes the information on the error back to the base agent for it to try again.

So that's trae-agent in a nutshell. Superb! I have screwed and chopped their source code entirely for learning purposes.



# Lord help me but I'm back to the old me

I've just written an extremely lengthy blog post by chopping up pieces of the `trae-agent` base agent code. The blog post is longer than the code now lol. Oh well! This post isn't built to be read as much as I'm building it to write it.


I needed a better understanding of trae agent and now I have it.


So let's TL;DR; trae-agent for those who want to skip to the bottom so I can edit this and put it up at the top.


1. Create a task for the issue
2. Start calling the LLM with the available tools
3. Run tools with arguments from LLM and reflect if they error out
4. Evaluate whether the task is done 

Each time it's iterating through the steps of completing a task it's doing 2-4.

```{mermaid}
flowchart TD
    A["Start Execution"] --> B["Initialize task and messages"]
    B --> C{"step <= max_steps?"}
    C -- No --> D["Task failed: max steps exceeded"]
    C -- Yes --> E["LLM generates response with tools"]
    E --> F{"LLM indicates task completed?"}
    F -- Yes --> G{"Actual completion check?"}
    G -- Yes --> H["Finalize and break loop"]
    G -- No --> I["Send task incomplete message"]
    I --> C
    F -- No --> J["Process tool calls"]
    J --> K{"Parallel or sequential?"}
    K -- Parallel --> L["Execute in parallel"]
    K -- Sequential --> M["Execute sequentially"]
    L --> N["Record results"]
    M --> N
    N --> O{"Any errors?"}
    O -- Yes --> P["Generate reflection with errors"]
    P --> Q["Add reflection to messages"]
    O -- No --> Q
    Q --> C
    H --> R["Execution success"]
    D --> S["Return execution result"]
    R --> S
    S --> T["Display summary"]
```


LMFAO I'm not too proud to say I got the LLM to generate my mermaid and it's so detailed hahaha.

Oh well! It's not wrong! And each time through the loop it's adding the subsequent calls to the list of messages.

# Infrastructure

The cheaper spools of generic PLA without carbon fiber in them showed up and I've been printing since Friday afternoon. I've made a complete tower in that time. I sort of want to fast forward to the dual sided towers because they are so much more efficient money wise. Half the cost per planting site. Just put lights up against the wall instead of towers. But I've sunk a bunch into the single sided ones so I want to do at least a good sized chunk of single sided towers. Maybe two or three only, just because they're the test bed.

It's time to start thinking about a transfer pump and putting together a wooden rack for the towers and gutters to hang and rest on. Real simple. Just a frame for hanging towers and lights (and probably fans). I'm going to put it together with screws so I can remove in the future if we want to do something different with that room and reassemble somewhere else.


I __really__ need a big metal building for my factory ambitions. Somewhere for towers and big machines that make PVC components (including grow towers!) and my CNC equipment I want to invest in.

I have a dream of a CNC company a lot like [Langmuir Systems][langmuir] except it's remote oriented and everyone who becomes an employee/co-owner has a big metal building on their rural acreage that's full of every piece of equipment in the catalog in robotic workcells churning away making random parts and also 
> every piece of equipment in the catalog!

That's what CNC and metal fab bring. Yeah eventually go all in with a metal printer, but there's a ton you can do with just a plasma bed and a CNC press brake.

Shit the gantry mill is only $4495 for a limited time. Oh god I want one so bad. I need somewhere to put it first. I don't care if I never use it for a productive purpose it would be fucking rad to have and I imagine there are all kinds of positive knock-on effects for having your own little means of production in a few big metal buildings on the compound.



# Projects

## In General
Where we are now
:::{figure} ../images/round-table-projects.png
Progress is fucking slow
:::


:::{figure} ../images/round-table-agents.png

Locked in — where we want to be
:::
:::::::{div}  
:class: col-body-inset-right

:::::{important}
Where you been fool?
:::::

:::::::

:::::::{div}
:class: col-body-inset-left

:::::{tip}
> I been chilling with my agents.
:::::

:::::::

## In Actual

- sim2real — I started making a URDF with the camera positions but now have a STL alignment problem
- hydroponics — I've started using cheaper filament and printing two segments fused together
- ai assistant — I have been experimenting with [`trae-agent`][base-agent-trae]
- math book — I found [a site][jiha-kim-na-courses] that's already doing a lot of what I want to do so that's good — there is also this blog post
- infrastructure — I haven't done any work on updating the slurm cluster but I did some research into how to network together five hypothetical GX10s

--- 

I guess eventually I will need to branch off and start having a project page where I can keep status updates for the projects and god forbid any actual deliverables that come as a result of them.


But I'm not just posting tweets about this on atproto. I'm actually documenting things and using them to further my understanding. I mean this post is basically me going through and reading the code and vomiting it out for a good bit. That's how you learn.


[auto-urdf]: https://arxiv.org/abs/2412.05507v1
[infinigen]: https://github.com/princeton-vl/infinigen/blob/main/docs/ExportingToSimulators.md
[bash-tool-trae]: https://github.com/bytedance/trae-agent/blob/main/trae_agent/tools/bash_tool.py
[base-agent-trae]: https://github.com/bytedance/trae-agent/blob/main/trae_agent/agent/base.py
[langmuir]: https://www.langmuirsystems.com/
[a2a-project]: https://github.com/a2aproject/A2A
[jiha-kim-na-courses]: https://jiha-kim.github.io/crash-courses/numerical-analysis/index/