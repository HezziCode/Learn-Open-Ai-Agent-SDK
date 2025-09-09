from agents import Agent, Runner, ModelSettings, ReasoningItem
from config import run_config
from tool import add, sub, mul, div 
import asyncio

agent = Agent(
    name="Huzaifa Agent!",
    instructions="You are Helpful math teacher and reply general questions as well generate paragraph as well like whatever user say you have to do it!",
    tools=[add, sub, mul, div],



    model_settings=ModelSettings(
        # truncation is "auto" by default.      
        # Controls behavior when total tokens (input + history) exceed the model's limit (~128k for gpt-4o-mini):
        # - "auto": older conversation content is truncated (dropped) so the request still succeeds.
        # - "disabled": nothing is truncated; if tokens exceed the limit, the API will fail with an error.
        #truncation="disabled",



        # By default its None
        # max_tokens controls the length of the model's output.
        # You can limit how long the response is—if you don't want a very long output,
        # set max_tokens to a smaller number.
        #max_tokens=12,



        # By default, reasoning is None (disabled). 
        # Requires OpenAI API support. 
        # When turned on, the model thinks through multiple steps by itself
        # before giving the final answer.

        # reasoning = {
        #     "strategy": "step_by_step",
        #     "depth": 2,
        #     "effort": "high"   
        # },



        # By default, verbosity is None. 
        # Requires OpenAI API support. 
        # It controls the length/detail of the model's responses:
        # - 'low' -> short answers
        # - 'medium' -> medium-length answers
        # - 'high' -> long/detailed answers
        # If None, the agent decides the appropriate response length automatically.

        # verbosity="medium",


         parameters={
             # frequency_penalty is 0.0 by default and ranges from -2.0 to 2.0.
             # Its purpose is to reduce repeated use of the same words many times.
             # - At 0.0: the model can naturally repeat words when needed.
             # - At higher values (e.g., 1.0 or 2.0): the model avoids repeating words too often,
             # - encouraging more varied phrasing instead of repetition.
             # - At negative values (e.g., -1.0): the model is more likely to repeat words frequently.

             #"frequency_penalty": 1.99,
        }
    )
    )

async def main():
    # max_turns is the number of times the agent will run by default it is 10
    res = await Runner.run(starting_agent=agent, max_turns=2, input="Give me 5 unusual and creative names for a coffee shop, make them funny and imaginative.", run_config=run_config)
    print(res.final_output)


asyncio.run(main())
