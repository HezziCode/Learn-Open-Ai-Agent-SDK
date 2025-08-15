# Agent Configuration Patterns

## What It Is

Simple, runnable examples that show two ways to configure AI agents: a single global model shared by many agents, or per‑agent models when you want different providers/capabilities. It also includes a tiny prompt router that picks which agent should handle a request.

## What It Does

- Demonstrates global config: multiple agents reuse one Groq client/model.
- Demonstrates agent-level config: separate Groq and Gemini models with basic keyword routing.

## Why It’s Useful

Global config keeps things fast and simple when agents can share the same model. Per‑agent config gives you flexibility to mix providers (e.g., math vs. image tasks) and route requests to the best tool for the job—all with minimal code changes.

## Example

```python
# Pseudocode sketch of routing
if looks_like_image_request(user_input):
    run(image_agent)
else:
    run(math_agent)
```
