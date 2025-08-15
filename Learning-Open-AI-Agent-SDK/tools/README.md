# Agent Tools

## What It Is

A minimal example of giving an agent callable Python functions (tools) to perform reliable, deterministic tasks—like math—alongside LLM reasoning.

## What It Does

- Registers add, sub, mul, div as @function_tool() helpers and wires them into an Agent.
- Runs the agent so it can decide when to call a tool and include the tool’s result in its final answer.

## Why It’s Useful

Tools let agents offload precise work to real code instead of relying on the model to “guess.” This boosts accuracy, keeps answers consistent, and lets you integrate domain logic safely.

## Example

```python
from agents import function_tool

@function_tool()
def add(a: int, b: int) -> str:
    return f"the sum of {a} and {b} is {a+b}"
```
