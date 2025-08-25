from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool
from config import config, model
import asyncio
from tools.agent_tool import fetch_user_data, fetch_user_data_by_id, math_expert

enable_verbose_stdout_logging()

fetch_user_data_agent = Agent(
    name="Teacher Huzaifa's Agent",
    instructions="You are a teacher. Answer the questions based on the context. and give the details about tool that fetch data",
    model=model,
    tools=[fetch_user_data, fetch_user_data_by_id]
) 


math_agent = Agent(
    name="Math Agent",
    instructions="You are a math agent. Answer the questions based on the context.",
    model=model,
    tools=[math_expert]
)

Orchestrator_agent = Agent(
    name="Orchestration Agent",
    instructions="You are an orchestration agent. You can call other agents to help you answer the questions.",
    model=model,
    tools=[
        fetch_user_data_agent.as_tool(
            tool_name="Fetch_data", 
            tool_description="Fetch the user data from fetch_user_data function, fetch_user_data_by_id function"
            ),
            math_agent.as_tool(
                tool_name="Math_Agent",
                tool_description="Answer the math questions based on the context."
            )]
)

async def main():
    prompt = input("Ask Everything: ")
    runner = await Runner.run(starting_agent=Orchestrator_agent, input=prompt, run_config=config)
    print(runner.final_output)

asyncio.run(main())