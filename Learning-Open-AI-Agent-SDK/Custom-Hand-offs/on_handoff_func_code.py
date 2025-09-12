from agents import RunContextWrapper
from input_data_pydantic import InputDataSchema

# This function runs first when a handoff is triggered. 
# We can use it for data fetching, manipulation, database operations, or logging.

# <---->    <---->    <---->    <---->    <---->    <---->     <---->     <---->     <---->


# input_data: When the main_agent hands off to an expert agent, it may need extra context 
# It may like (advice, result, reason, summary, etc.) to understand how to perform the task. 
# This input_data comes from the main (triage_agent) who assigned the task.

async def on_handoff_func_code(ctx: RunContextWrapper, input_data: InputDataSchema):
    print(ctx.context)


    # Changing schema wording also changes agent communication. 
    # Example:

    print(input_data.reason) # → gives the reason
    # print(input_data.result) → gives the answer
    # print(input_data.advice) → gives the advice but it’s up to the LLM whether to provide advice or a direct answer.