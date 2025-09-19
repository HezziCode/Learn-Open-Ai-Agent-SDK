from agents import Agent, AgentHooks, RunContextWrapper, TContext, Tool
from typing import Any
import requests

# Base class for adding custom logic (hooks) to an Agent’s workflow
# A base class to let you add custom behavior to an Agent

class MyAgentHooks(AgentHooks):
    # Called when the agent starts                           # The current agent instance (e.g. assistant_agent)  
    async def on_start(self, ctx:RunContextWrapper[TContext], agent:Agent) -> None:
        print("Agent started")
        print(f"starting context: {ctx.context}") # Get the context
        ctx.context["email"] = "abc@gmail.com" # We add email to the context

        url = f"https://jsonplaceholder.typicode.com/users/{ctx.context['id']}"
        response = requests.get(url)
        result = response.json()
        ctx.context["fetch_user_data"] = result


    # Called when the agent ends                                        # final result output type check from the agent      
    async def on_end(self, ctx:RunContextWrapper[TContext], agent:Agent, output:Any) -> None:
        print("Agent ended")
        print(f"ending context: {ctx.context}") 



    # Called when a tool starts                                                # The tool instance
    async def on_tool_start(self, ctx:RunContextWrapper[TContext], agent:Agent, tool:Tool) -> None:
        print("Tool started")



    # Called when a tool ends                                                # The tool result
    async def on_tool_end(self, ctx:RunContextWrapper[TContext], agent:Agent, tool:Tool, result:str) -> None:
        print("Tool ended")



    # Called when the agent hands off to another agent  -> # the agent receiving the handoff || the agent that handed over the task  <- about source parameter          
    async def on_handoff(self, ctx:RunContextWrapper[TContext], agent:Agent, source:Agent) -> None:
        print("There is only Handoff")
