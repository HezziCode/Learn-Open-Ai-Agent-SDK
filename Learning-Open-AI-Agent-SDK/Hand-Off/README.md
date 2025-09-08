## Handoff — what was implemented

This project demonstrates a simple "handoff" workflow between agents: one assistant agent delegates tasks to specialist agents (Math and English). The handoff is implemented so the assistant can pass a task to a more appropriate agent and receive the final result.

### Key parts (short)

- `assistant_agent` — the delegator. It contains `handoffs=[math_agent, english_agent]` and a `handoff_description` that explains its role.
- `math_agent` and `english_agent` — specialist agents. Each has its own `handoff_description` and instructions.
- `plus` tool (`tool.py`) — a small helper function used by the Math agent to compute sums.
- `RECOMMENDED_PROMPT_PREFIX` — added to agent instructions so agents know they are part of a multi-agent workflow and can perform/accept handoffs.

### How handoff works (plain)

1. The Assistant Agent receives a request.
2. It decides the best specialist to handle the task (Math or English) using the configured handoffs.
3. The selected agent runs and may call a tool (for example `plus`) to produce the final answer.
4. The program prints the last agent name and the final output so you can see which agent completed the task.

### Run and observe

Run the main script from this folder. Example commands you may use:

```bash
uv run agent.py
```

Expected simple output (example for input `what is 2+2?`):

- Last Agent name is Math agent
- Your answer is 4

### One-line summary in Urdu (Roman)

Handoff ka matlab: ek assistant agent task dosray (specialist) agent ko pass karta hai taake woh behtar jawab de sake.
