from agents import Agent, Runner, trace
from config import config
from tool import plus


math_agent = Agent (
    name="Math Agent",
    instructions="You are a helpful math assistant",
    tools=[plus],
    handoff_description="This is math teacher expert."
)



assistant_agent = Agent (
    name="Assistant Agent",
    instructions="You are a helpful assistant your task to delegate tasks to other agents.",
    handoffs=[math_agent]
)


# Higher-level tracing:
# Putting the whole while-loop inside `with trace("Learning Tracing")`
# means all user messages and agent runs are saved inside ONE trace.
# If we don’t do this, each run will make its own separate trace.

with trace("Learning Tracing"):
    while True:
        prompt = input("User: ")

        if prompt == "exit":
            print("Bye!")
            break

        result = Runner.run_sync(starting_agent=assistant_agent, input=prompt, run_config=config)


        print(result.last_agent.name)
        print(result.final_output)
