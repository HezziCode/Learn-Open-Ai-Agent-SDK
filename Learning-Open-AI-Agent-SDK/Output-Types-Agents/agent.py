from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, AsyncOpenAI
from dotenv import load_dotenv
import os
from data_classes import Config
from pydantic_config import Output_config


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    tracing_disabled=True
)

agent = Agent(
    name ="Huzaifa's Agent",
    instructions="You are a helpful assistant.",
    model=model,
    output_type=Output_config
)

result = Runner.run_sync(agent, "just tell me what the answer of 2 + 2", run_config=config)
print(result.final_output)
