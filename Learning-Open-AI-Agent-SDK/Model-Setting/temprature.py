from agents import Agent, Runner, ModelSettings
from config import run_config
from tool import add, sub, mul, div 
import asyncio

agent = Agent(
    name="Huzaifa Agent!",
    instructions="You are Helpful math teacher and reply general questions as well generate paragraph as well like whatever user say you have to do it!",
    tools=[add, sub, mul, div],

    model_settings=ModelSettings(
        # temperature controls output style: closer to 0 → focused and simple,
        # # around 1 → balanced, closer to 2 → more creative and random
        temperature=0,

        # Just like temperature, top_p is another parameter that controls randomness
        # but in a slightly different way.

        # top_p controls word choice: near 0 → pick only the most likely word,
        # near 1 (by_default) → more natural variety

        top_p=1
    )
    )

async def main():
    # max_turns is the number of times the agent will run by default it is 2
    res = await Runner.run(starting_agent=agent, max_turns=2, input="Give me 5 unusual and creative names for a coffee shop, make them funny and imaginative.", run_config=run_config)
    print(res.final_output)

asyncio.run(main())