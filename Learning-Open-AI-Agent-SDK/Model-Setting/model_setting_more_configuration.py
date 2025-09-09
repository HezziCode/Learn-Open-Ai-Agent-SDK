from agents import Agent, Runner, ModelSettings
from config import run_config
from tool import add, sub, mul, div 
import asyncio

agent = Agent(
    name="Huzaifa Agent!",
    instructions="You are Helpful math teacher and reply general questions as well generate paragraph as well like whatever user say you have to do it!",
    tools=[add, sub, mul, div],
    # We can see this agent name in tracing by default its agent workflow but after this setting
    # agent name change to test_agent

    # meta_data={"project":"test_agent"}

    model_settings=ModelSettings(
        # By default, `store` is None. 
        # If set to True, the system prompt, user prompt, and agent output 
        # are saved in the OpenAI dashboard, allowing you to view the 
        # agent's behavior in tracing and logs.

        # store=True


        # include_usage: By default None. 
        # This only works with the raw Chat Completions API (not with Agent SDK). 
        # If set to True, the response includes usage info (tokens used, etc.) 
        # which you can see in the API response. 
        # Note: In Agent workflows, this field is ignored and usage is not returned.

        # include_usage=True


        # response_include: By default None. 
        # This works only with the raw Chat Completions API (not with Agent SDK).
        # You can pass a list like ["usage", "logprobs"] to include extra details 
        # in the API response. 
        # - "usage" → token counts (prompt, completion, total). 
        # - "logprobs" → model's confidence for each generated token. 
        # Useful for debugging, research, or tracking costs. 

        # response_include=["usage", "logprobs"]



        # top_logprobs: By default None. 
        # Only works with the raw Chat Completions API (not with Agent SDK).
        # Example: if top_logprobs=5 → model may return:
        # "the" (0.45), "a" (0.20), "this" (0.15), "one" (0.10), "that" (0.05).

        # top_logprobs=3



        # extra_query: By default None.
        # Lets you send extra parameters (like temperature, top_p, penalties, etc.) 
        # along with the system prompt, user prompt, and tool schema.
        # Note: Only works with the raw Chat Completions API (not Agent SDK).
        # as **query parameters in the request URL**

        #extra_query={"temperature":0.5, "top_p":0.7,"presence_penalty": 1.0}


        # extra_body: By default None.
        # Lets you send extra parameters (like temperature, top_p, penalties, etc.) 
        # along with the system prompt, user prompt, and tool schema.
        # Note: Only works with the raw Chat Completions API (not Agent SDK).
        # as **JSON fields in the request body**

        #extra_body={"temperature":0.5, "top_p":0.7,"presence_penalty": 1.0}


        # extra_headers: By default None.  
        # Lets you send extra/custom HTTP headers with your API request.  
        # Normally, headers already include Authorization (API key) and Content-Type.  
        # But if you need to add more (like X-Custom-Header, X-Trace-ID, etc.),  
        # you can provide them here.  
        # Note: Only works with raw Chat Completions API (not Agent SDK).  

        # extra_headers= {"X-Custom-Header": "HuzaifaAgent", "X-Trace-ID": "12345"}




        # extra_args: By default None.
        # Lets you pass additional keyword arguments directly into the SDK's function call.
        # Example:
        #   extra_args={"frequency_penalty": 0.8, "temperature": 0.5}
        #   → becomes equivalent to:
        #     openai.ChatCompletion.create(model="gpt-4", messages=[...], frequency_penalty=0.8, temperature=0.5)
        #
        # Difference:
        # - extra_query → parameters are sent in the URL query string (e.g., ?temperature=0.5&top_p=0.7).
        # - extra_body  → parameters are sent inside the JSON request body.
        # - extra_args  → parameters are passed directly as function arguments in the SDK call.
        #
        # Note: Only works with raw Chat Completions API (not Agent SDK).

        # extra_args={"temperature":0.5, "top_p":0.7}





        # resolve(): 
        # Creates a new ModelSettings by merging this instance with an override.
        # Any non-None values in the override replace the existing ones.
        #
        # Example:
        # base = ModelSettings(temperature=0.7, top_p=0.9, store=None)
        # override = ModelSettings(temperature=0.3, store=True)
        # final = base.resolve(override)
        # → final.temperature = 0.3 (override applied)
        # → final.top_p = 0.9 (base kept, since override was None)
        # → final.store = True (override applied)


#     Base settings (default)
#     base_settings = ModelSettings(
#         temperature=0.7,
#         top_p=0.9,
#         store=None
# )

#     Override settings ()
#     override_settings = ModelSettings(
#         temperature=0.3,   # that's going to override 
#         store=True         # that's also gonna override
#      top_p is None here, so it will be ignore
# )

#     Resolve it
#     final_settings = base_settings.resolve(override_settings)

#     print(final_settings.temperature)  # 0.3  (override ho gaya)
#     print(final_settings.top_p)        # 0.9  (base ka value reh gaya)
#     print(final_settings.store)        # True (override ho gaya)
         ) 
    )

async def main():
    # max_turns is the number of times the agent will run by default it is 10
    res = await Runner.run(starting_agent=agent, max_turns=2, input="Write a 200-word paragraph repeating 'dragon' many times.", run_config=run_config)
    print(res.final_output)

asyncio.run(main())



# Model setting topic end hope You learn something from this code! Happy coding :)
