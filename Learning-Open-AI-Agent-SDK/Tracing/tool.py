from agents import function_tool

@function_tool
def plus(a:int, b:int):
    """Add two numbers."""
    return a + b