from agents import Agent, RunContextWrapper 
from user_data_type_using_pydantic import UserDataType 

# This is the LLM context where we give our data to agent/LLM
def dynamic_instructions(ctx:RunContextWrapper[UserDataType], agent:Agent[UserDataType]):
    return f"User name is {ctx.context.name}, you are a helpful assistant."