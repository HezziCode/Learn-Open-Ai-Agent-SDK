## Agent as a Tool

### What It Is

A simple way to let one agent use another agent like a tool. The main agent (orchestrator) can call a smaller agent that has its own job and tools.

### What It Does

- Turns a full agent into a tool with as_tool(name, description)
- Lets the orchestrator choose the right agent-tool based on the user’s request
- Keeps each skill (like “fetch users” or “do math”) in its own agent

### Why It’s Useful

- Easy to understand: each agent has one clear job
- Easy to grow: add new skills by adding new agents
- Easy to reuse: the same agent can be used in many places

### Example

```python
# Conceptual sketch
from agents import Agent
from tools.agent_tool import fetch_user_data, fetch_user_data_by_id, math_expert

# Two small agents
data_agent = Agent(name="Data Agent", instructions="Fetch user data.", tools=[fetch_user_data, fetch_user_data_by_id])
math_agent = Agent(name="Math Agent", instructions="Solve simple math.", tools=[math_expert])

# Orchestrator that calls them as tools
orchestrator = Agent(
    name="Orchestrator",
    instructions="Pick the right helper agent.",
    tools=[
        data_agent.as_tool("Fetch_data", "Get users or a user by id"),
        math_agent.as_tool("Math_Agent", "Answer basic math questions"),
    ],
)
```

### After the Example (Quick Notes)

- The orchestrator reads the user’s request and decides which agent-tool to call
- data_agent handles user data (get all users or one user by id)
- math_agent handles basic math questions
- You can add more agents later (for example, a Weather Agent) and expose it with as_tool
- Clear tool descriptions help the orchestrator choose the right agent
