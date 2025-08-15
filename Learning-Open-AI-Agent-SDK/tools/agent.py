from agents import Agent, Runner, enable_verbose_stdout_logging
from tools.math_tools import add, sub, mul, div
from config import config, model
import asyncio

enable_verbose_stdout_logging()

agent = Agent(
    name="Teacher Huzaifa's Agent",
    instructions="You are expert in math problems and you are a math teacher for now but you can answer other different topic as well.",
    model=model,
    tools=[add, sub, mul, div]
) 

async def main():
    prompt = input("Ask Everything: ")
    runner = await Runner.run(starting_agent=agent, input=prompt, run_config=config)
    print(runner.final_output)

asyncio.run(main())