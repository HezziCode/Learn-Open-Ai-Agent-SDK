# Output Types

## What It Is

A pattern for making agents return structured, predictable data. You define an output schema (using a simple model), and the agent’s response is validated and returned as a typed object rather than free‑form text.

## What It Does

- Lets you define a strict output schema (e.g., fields like n1, n2, result) so responses come back as typed values.
- Runs the agent and validates the response against that schema, returning final_output as a typed object your code can use directly.

## Why It’s Useful

Structured outputs are easier to test, log, and compose with other code. They reduce parsing errors and make it clear what the agent must return, which helps with reliability in larger systems.

## Example

```python
# Conceptual sketch
class Output(BaseModel):
    n1: int
    n2: int
    result: int

agent = Agent(output_type=Output)
print(Runner.run_sync(agent, "Add 2 and 2").final_output)
```
