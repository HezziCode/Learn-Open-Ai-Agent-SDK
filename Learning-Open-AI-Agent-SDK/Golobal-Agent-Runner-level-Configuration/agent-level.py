from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
import os
import asyncio  

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set")
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not set")


groq_client = AsyncOpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
    )
  
gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta"
    )  


groq_model = OpenAIChatCompletionsModel (
    model="llama-3.3-70b-versatile",
    openai_client=groq_client
) 

gemini_model = OpenAIChatCompletionsModel (
    model="gemini-2.0-flash",
    openai_client=gemini_client
) 


math_agent = Agent(  
    name="MathAgent",  
    instructions="Math problems solve karo step-by-step.",  
    model=groq_model  
)  
image_agent = Agent(  
    name="ImageAgent",  
    instructions="Image banao like you can with ascii or image descriptions banao.",  
    model=gemini_model  
)  

checking_prompt_agent = Agent(
    name="CheckingPromptAgent",
    instructions="""
You are a strict classifier.

Your task is to read a user prompt and determine:
- Return **only** `math` if it's a math-related question or problem.
- Return **only** `image` if it's asking to describe or imagine a visual or scene.

Do not add anything else. Just return `math` or `image`.
""",
    model=groq_model
)


async def main():
    question = input("Enter your Prompt: ")

    if any(word in question.lower() for word in ["image", "photo", "picture", "describe"]):
        result = await Runner.run(input=question, starting_agent=image_agent)
    else:
        result = await Runner.run(input=question, starting_agent=math_agent)

    print(result)

asyncio.run(main())