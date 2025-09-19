from agents import function_tool

@function_tool
def plus(a:int, b:int) -> str:
    """Add two numbers."""
    print("Plus tool fire ------------------>")
    return a + b