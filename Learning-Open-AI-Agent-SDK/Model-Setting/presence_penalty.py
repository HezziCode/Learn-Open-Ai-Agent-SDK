from agents import Agent, Runner, ModelSettings
from config import run_config
from tool import add, sub, mul, div 
import asyncio

agent = Agent(
    name="Huzaifa Agent!",
    instructions="You are Helpful math teacher and reply general questions as well generate paragraph as well like whatever user say you have to do it!",
    tools=[add, sub, mul, div],

    model_settings=ModelSettings(
        # presence_penalty is 0.0 by default and ranges from -2.0 to 2.0.
        # Its purpose is to encourage the model to talk about new topics/words.
        # - At higher values (e.g., 1.0 or 2.0): the model is pushed to avoid reusing words it already mentioned,
        #  and instead introduce new or different words.
        # - At negative values (e.g., -1.0): the model is more likely to repeat words.
        # presence_penalty=1.99


        # This means that the agent will not use any tools if tool_choice is set to "none"
        # tool_choice="none",  Or if you pass a specific tool name (e.g., tool_choice="sub"), the agent will only use that tool and will not automatically run any other tools.
        # reset_tool_choice=True, # After using a tool once, the agent resets to "auto" and may default to LLM next turn instead of the tool.
        ) # parallel_tool_calls=True : This will give you power to call tool parallel but you have to get an OpenAI API key Other it will not work by default its True
    )

async def main():
    # max_turns is the number of times the agent will run by default it is 10
    res = await Runner.run(starting_agent=agent, max_turns=2, input="Write a 200-word paragraph repeating 'dragon' many times.", run_config=run_config)
    print(res.final_output)

asyncio.run(main())
