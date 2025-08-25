import requests 
from agents import function_tool


@function_tool()
def fetch_user_data() -> list:
    """Fetch function for the user data and return it as a list"""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

@function_tool()
def fetch_user_data_by_id(id: int) -> list:
    """Fetch function for the user data and return it as a list"""
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    return response.json()

@function_tool
def math_expert(question: any) -> any:
    """A math expert that can solve any math problem"""
    return f"Solved answer for: {question}"