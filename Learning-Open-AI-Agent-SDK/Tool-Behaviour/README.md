# Tool Behavior — Core Features

### What It Is
A small demo repo that shows how tool-based behavior and model settings work.  
It’s not a full agent design doc — just a lightweight example project.  


### Why It’s Useful
- Easy to see how function tools are registered and called  
- Lets you experiment with tool choice behaviors (`auto`, forced, reset)  
- Makes it simple to test different tool stopping policies  
- Provides a minimal but working setup for playing with the `openai-agents` library  

## Key files

- `tool.py` — example tools implemented with `@function_tool()` (math helpers). Keep tool implementations small and return plain strings.
- `agent.py` — small usage example that creates an `Agent` instance, configures `ModelSettings`, and calls `Runner.run`. This file demonstrates how to wire tools into an agent run, but omits deep agent internals.
- `config.py` — runtime configuration: initializes the async model client and `RunConfig`. It expects `GEMINI_API_KEY` in the environment.
- `pyproject.toml` — lists the primary dependency: `openai-agents`.



### Example

```python
agent = Agent(
    name="Huzaifa Agent!",
    instructions="You are Helpful math teacher",
    tools=[add, sub, mul, div],
    # This means that the agent will stop after the first tool use and give you the final output.
    # tool_use_behavior="stop_on_first_tool",
    # This means that the agent will stop after the tool "multiply" and give you the final output.
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["add", "mul"]),
    # This means that the agent will not use any tools if tool_choice is set to "none"
    model_settings=ModelSettings(
        tool_choice="sub",
        reset_tool_choice=True, # As far as i understand this will reset tool choice to auto after first tool use
        ) # parallel_tool_calls=True : This will give you power to call tool parallel but you have to get an OpenAI API key Other it will not work
    )
