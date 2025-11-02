---
date: "2025-10-19"
title: "Weekend Build: Creating a Julia Native LangGraph Alternative"
---

# Weekend Build: Creating a Julia Native LangGraph Alternative

I spent this weekend [building][julia-agent-exploration] something I've been thinking about for a while: a Julia-native alternative to Python's LangGraph framework. This wasn't about porting LangGraph to Julia - it was about creating something that leverages Julia's unique strengths while maintaining the core patterns that make LangGraph useful.

## The Core Problem I Was Trying to Solve

LangGraph has some great patterns for building agent systems:
- State management with automatic message merging
- Single-turn execution with conversation history accumulation
- Clean routing between nodes that only take state as input
- Tool calling for structured decision making

But Python has limitations: runtime type checking, asyncio complexity, and no native support for the kind of mathematical reasoning that Julia excels at.

## What I Actually Built

### 1. JuliaLangGraph.jl - The Core Framework

The main deliverable is a clean, minimal implementation that captures the essence of LangGraph's single-turn execution pattern:

```julia
mutable struct AgentState
    messages::Vector{Dict{String, Any}}
    input::String
    decision::String
    output::String
    task_completed::Bool
end
```

Key features:
- **State Management**: Automatic message merging (Julia's equivalent of Python's `operator.add`)
- **Single-Turn Execution**: The `invoke()` function runs the graph exactly once per call
- **Conversation History**: Messages accumulate across multiple invocations
- **LLM Integration**: Uses tool calling for reliable routing decisions

The critical insight was that nodes should only take state as input and return updates, exactly like LangGraph. The LLM client gets captured in closures during graph construction.

### 2. SimpleAgent.jl - Tool Integration Framework

The second major piece is a tool system that automatically generates schemas from Julia functions:

```julia
@tool function web_search(query::String, max_results::Int = 5)
    # Search implementation
end
```

This uses Julia's introspection capabilities to:
- Extract parameter names and types from function signatures
- Pull descriptions from docstrings
- Generate JSON schemas automatically
- Register tools in a global registry

The `@tool` macro handles all the boilerplate, making it trivial to add new capabilities.

## Technical Challenges I Solved

### 1. State Merging Semantics

Getting the message accumulation right was tricky. In Python LangGraph, you use `operator.add` for messages. In Julia, I implemented:

```julia
function merge_state!(state::AgentState, updates::Dict)
    for (field, value) in updates
        if field == "messages" && isa(value, Vector)
            append!(state.messages, value)  # Like operator.add
        elseif hasfield(AgentState, Symbol(field))
            setfield!(state, Symbol(field), value)
        end
    end
end
```

### 2. Tool Schema Generation

Julia's reflection capabilities are powerful but complex. I had to dig into:
- `Base.arg_decl_parts()` for parameter names
- `Base.Docs.meta` for docstring extraction
- Type system introspection for schema generation

### 3. LLM Integration quirks

The z-ai/glm-4.6 model has inconsistent support for `response_format` in chat mode, but tool calling works reliably. I structured the routing around forced tool usage:

```julia
response = create_chat(
    llm_client,
    "z-ai/glm-4.6",
    messages;
    tools=[routing_tool],
    tool_choice="required"  # Force tool usage
)
```

## What Works Right Now

### ✅ JuliaLangGraph.jl
- State management with proper message accumulation
- Single-turn graph execution
- LLM-based routing with tool calling
- Clean node definition pattern

### ✅ SimpleAgent.jl
- Automatic tool schema generation
- `@tool` macro for easy tool registration
- Real web search integration
- Function introspection system

### ✅ Core Patterns Implemented
- State-only node functions
- Conditional routing with LLM decisions
- Message history accumulation
- Tool-based decision making

## What's Still a Work in Progress

### 🚧 Testing Infrastructure
I need comprehensive tests for:
- State merging edge cases
- Tool schema generation accuracy
- LLM routing reliability
- Error handling patterns

### 🚧 Agent Wrapper
The core `invoke()` function works, but I want a cleaner `Agent` wrapper:
```julia
agent = Agent(graph)
response = agent.execute("Tell me a joke about programming")
```

### 🚧 Performance Optimization
While Julia should be faster, I haven't benchmarked it yet against equivalent Python implementations. The theoretical advantages are there, but I need real measurements.

### 🚧 Advanced Patterns
I want to explore:
- Evaluator-optimizer patterns
- Parallel execution patterns
- Symbolic computation integration
- Type-safe state transitions

## Key Insights from the Build

### 1. Julia's Strength is in the Details
The combination of multiple dispatch, strong typing, and metaprogramming creates possibilities that don't exist in Python. Even in this simple implementation, I can see paths to optimizations that would be impossible in LangGraph.

### 2. Tool Integration Can Be Elegant
The `@tool` macro approach feels very Julian - zero-cost abstractions where the framework gets out of your way. Automatic schema generation from function signatures and docstrings is something I haven't seen done this cleanly elsewhere.

### 3. State Management is Universal
The core patterns from LangGraph translate well to Julia. The idea of state-only functions that return updates, single-turn execution, and message accumulation are language-agnostic concepts that work beautifully in Julia.

### 4. LLM Integration is the Hard Part
The most challenging aspect was working around model limitations and API quirks. Tool calling proved more reliable than structured JSON output, which is an important lesson for anyone building agent systems.

## The Code Structure

```
julia_agent_exploration/
├── JuliaLangGraph/
│   └── src/JuliaLangGraph.jl     # Core framework
├── SimpleAgent/
│   └── src/SimpleAgent.jl        # Tool system
├── examples/                     # Usage examples
└── docs/
    └── FINAL_SUMMARY.md          # Technical details
```

Both packages are functional but still evolving. The core concepts work, but there's room for refinement and additional features.

## Why This Matters

This isn't just about recreating LangGraph in Julia. It's about exploring what's possible when you design agent systems from the ground up with Julia's capabilities in mind:

- **Type Safety**: Compile-time checking prevents entire classes of runtime errors
- **Performance**: JIT compilation and native code generation
- **Mathematical Reasoning**: Integration with Symbolics.jl for optimization
- **Metaprogramming**: Macros and code generation for elegant abstractions

## Next Steps

This weekend was about getting the core patterns working. The next phase will focus on:

1. **Testing**: Comprehensive test suite for reliability
2. **Benchmarking**: Real performance comparisons
3. **Documentation**: Clear examples and tutorials
4. **Advanced Features**: Exploring Julia-specific optimizations
5. **Community**: Getting feedback and contributions

## Final Thoughts

Building this was a reminder that sometimes the most valuable work is creating foundational tools. While I didn't create something revolutionary this weekend, I built a solid foundation that could grow into something genuinely useful for the Julia ecosystem.

The code is available on [GitHub](https://github.com/odellus/julia_agent_exploration) for anyone interested in exploring Julia-native agent systems. It's still a work in progress, but the core patterns work and demonstrate that there's real potential here.

**Time Invested:** Weekend (Saturday + Sunday)
**Current Status:** Functional prototype with room for growth
**Next:** Testing, benchmarking, and community feedback

---

*This project represents my exploration of what's possible when you rethink agent systems for Julia, rather than just porting patterns from Python. The journey is just beginning.*



[julia-agent-exploration]: https://github.com/odellus/julia_agent_exploration
