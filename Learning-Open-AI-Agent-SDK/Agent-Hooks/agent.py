import asyncio
from agents import Agent, Runner
from config import config
from agent_hooks import MyAgentHooks
from tool import plus


# Math Agent
# math_agent = Agent (
#     name="Assistant Agent",
#     instructions="You are a helpful math teacher.",
#     tools=[plus],
#     hooks=MyAgentHooks(),
#     handoff_description="This is math teacher."
# )


info = {"id": 3}

assistant_agent = Agent (
    name="Assistant Agent",
    instructions="You are a helpful assistant",
  # handoffs=[math_agent],
    hooks=MyAgentHooks()

)


prompt = input("User: ")

async def main():
    result = await Runner.run(assistant_agent, input=prompt, run_config=config, context=info,)

    print(result.final_output)

asyncio.run(main())