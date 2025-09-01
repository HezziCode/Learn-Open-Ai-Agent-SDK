from agents import Agent, Runner, ModelSettings
from config import run_config
from agents.agent import StopAtTools
from tool import add, sub, mul, div 
import asyncio

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

async def main():
    # max_turns is the number of times the agent will run by default it is 2
    res = await Runner.run(starting_agent=agent, max_turns=10, input="What is the answer of 1+2 and then multiply it by 2", run_config=run_config)
    print(res.final_output)

asyncio.run(main())