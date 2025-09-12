from agents import Agent, RunContextWrapper
from user_data_type_pydantic import UserDataType


async def tool_validation(ctx:RunContextWrapper[UserDataType],agent:Agent[UserDataType]): # UserDataType is used here as a generic type to provide strong typing 
    # Using UserDataType as a generic ensures strong typing for ctx and agent
    if ctx.context["age"] >= 18:
        return True
    else:
        return False