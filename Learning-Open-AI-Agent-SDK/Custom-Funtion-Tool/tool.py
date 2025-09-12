from agents import RunContextWrapper, function_tool, FunctionTool
from tool_schema_pydantic import tool_schema
from validation import tool_validation
from typing import Any

# This is our customize function that we create using open ai agent sdk!

async def subtract_function(ctx:RunContextWrapper, arg):
    print("Subtract tool fire ---------------->")
    obj = tool_schema.model_validate_json(arg) # Pydantic + LLM, will ensure that both n1 and n2 must be provided
    return f"Your answer is {obj.n1-obj.n2}."

subtraction = FunctionTool(
    name="subtract", # The tool name cannot contain spaces, so we use underscores instead
    description="This is subtract tool",
    params_json_schema=tool_schema.model_json_schema(),  # JSON schema for LLM (our job is to call it here)
    on_invoke_tool=subtract_function,
    is_enabled=tool_validation # It means whether this function is active then it run or false means this function will not run! obviously by default its True
)


# -------------------------------------------------------------------------------


@function_tool(is_enabled=tool_validation)
def addition(n1 : int, n2 : int) -> str:
    """this is plus function its help to agent to plus activity
    
    args:
    n1: int
    n2: int
    return str
    """

    print("plus tool call")
    return f"Your answer is {n1+n2}"


# -------------------------------------------------------------------------------




def my_custom_error_function(context: RunContextWrapper[Any], error: Exception) -> str:
    print(f"A tool call failed with the following error: {error}")
    return "An internal server error occurred. Please try again later."


@function_tool(name_override="multiply_tool", description_override="This is multiply tool function", is_enabled=tool_validation, failure_error_function=my_custom_error_function)
def multiply(n1 : int, n2 : int) -> str:
    """this is multiply function its help to agent to multiply activity
    
    args:
    n1: int
    n2: int
    return str
    """

    print("multiply tool call")
    return f"Your answer is {n1*n2}"