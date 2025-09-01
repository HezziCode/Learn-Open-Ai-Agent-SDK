from agents import ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta"
    )

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

run_config = RunConfig(
    model=model,
    tracing_disabled=True,    
)