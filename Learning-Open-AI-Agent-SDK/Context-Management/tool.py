from agents import function_tool, RunContextWrapper
from user_data_type_using_pydantic import UserDataType

@function_tool
def get_age(ctx:RunContextWrapper[UserDataType]):
    """"Get age function"""
    print("Age tool call ----------------->")
    print(f"What is in the ctx ----------------> {ctx.context.role}")
    # There we shared the age with LLM using Function_Tool 
    # see the agent.py file where i create dictionary and now their we give the context means
    # only age to the LLM using Function_tool
    return f"I am {ctx.context.age}"