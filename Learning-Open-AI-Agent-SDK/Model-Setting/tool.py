from agents import function_tool

@function_tool()
def add(a: int, b:int) -> str:
    """Add two numbers and give the output"""
    return a+b

@function_tool()
def sub(a: int, b:int) -> str:
    """Subtract two numbers and give the output"""
    return a-b

@function_tool()
def mul(a: int, b:int) -> str:
    """Multiply two numbers and give the output"""
    return a*b

@function_tool()
def div(a: int, b:int) -> str:
    """Divide two numbers and give the output"""
    return a/b



