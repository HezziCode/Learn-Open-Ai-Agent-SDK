from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
import os
import asyncio

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Global configuration
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
    )
model = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile", 
    openai_client=client
    )

# Agents with global config
joke_agent = Agent(name="JokeAgent", instructions="Tell jokes.", model=model)
fact_agent = Agent(name="FactAgent", instructions="Share random facts.", model=model)
poem_agent = Agent(name="PoemAgent", instructions="Write short poems.", model=model)

async def run_agent(query, agent):
    result = await Runner.run(input=query, starting_agent=agent)
    return result.final_output or "No response."

async def main():
    query = input("Enter your query: ")
    output = await run_agent(query, joke_agent)  
    print(output)

if __name__ == "__main__":
    asyncio.run(main())