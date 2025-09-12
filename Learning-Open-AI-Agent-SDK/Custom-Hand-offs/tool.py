from agents import function_tool

@function_tool
def plus(n1 : int, n2 : int) -> str:
    """this is plus function its help to agent to plus activity
    
    args:
    n1: int
    n2: int
    return str
    """

    print("plus tool call")
    return f"Your answer is {n1+n2}"


@function_tool
def weather(city : str):
    """Weather tool"""
    print("weather tool call")
    return f"{city} sunny."
