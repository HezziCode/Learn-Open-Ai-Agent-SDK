from agents import Agent, Runner
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from tool import plus
from config import config


math_agent = Agent (
    name="Math agent",
    # RECOMMENDED_PROMPT_PREFIX is added before agent instructions
    # and tells the agent that it is part of a multi-agent workflow,
    # so it can understand and perform handoffs easily.
    instructions=f""" {RECOMMENDED_PROMPT_PREFIX}
    You are a helpful Math teacher    
    """,
    tools=[plus],
    handoff_description="This is a Math teacher."
)

english_agent = Agent (
    name="English Agent",
    # RECOMMENDED_PROMPT_PREFIX is added before agent instructions
    # and tells the agent that it is part of a multi-agent workflow,
    # so it can understand and perform handoffs easily.
    instructions=f""" {RECOMMENDED_PROMPT_PREFIX}
    You are a helpful English teacher    
    """,
    handoff_description="This is a English teacher."
)


# Handoffs allow agent to delegate task to other agent
# Handoffs are represent as a tool to LLM
assistant_agent = Agent (
    name="Assistant Agent",
    instructions=f""" {RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant agent    
    """,
    handoff_description="You are a helpful assistant agent your work is to delegate task to specialize agent",
    handoffs=[math_agent, english_agent]
)

result = Runner.run_sync(starting_agent = assistant_agent, input="what is 2+2?", run_config=config)

# with this we can see the last agent and with .name we can see the exact see the last agent name
print(f"Last Agent name is {result.last_agent.name}")
print(result.final_output)