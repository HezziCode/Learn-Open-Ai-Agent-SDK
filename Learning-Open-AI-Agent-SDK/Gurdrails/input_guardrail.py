# Import necessary modules for input guardrail functionality
from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner, input_guardrail
from config import config
from schema_pydantic import Input_guardrail_schema

# Create an AI agent specifically for checking input messages
# This agent determines if user messages are appropriate hotel-related queries
input_guardrail_agent = Agent(
    name="Input Guardrail",
    instructions="You are an input guardrail, Check hotel Hezzi quires.",
    output_type=Input_guardrail_schema  # Uses predefined schema for consistent output
)


# Decorator that marks this function as an input guardrail
@input_guardrail
async def input_guard_function(ctx: RunContextWrapper, agent: Agent, input):
    """
    Input guardrail function that checks user messages before they reach the main AI agent.

    Logic:
    - If message is about Hotel Hezzi: Allow (tripwire_triggered = False)
    - If message is NOT about Hotel Hezzi: Block (tripwire_triggered = True)
    """
    # Run the guardrail agent to analyze the input message
    result = await Runner.run(input_guardrail_agent, input=input, run_config=config, context=ctx.context)

    # Return guardrail decision
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # Tripwire triggers when query is NOT about hotel (blocks non-hotel queries)
        tripwire_triggered=not result.final_output.is_hotel_Hezzi_query
    )
