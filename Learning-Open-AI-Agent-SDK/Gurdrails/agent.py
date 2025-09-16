# Import necessary modules for AI agent and guardrails
from agents import Agent, Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from config import config
from input_guardrail import input_guard_function
from output_guardrail import output_guard_function

# === GUARDRAILS SYSTEM ===
# Guardrails are safety mechanisms that protect AI conversations

# INPUT GUARDRAIL: Checks user messages BEFORE AI processes them
# - Allows hotel-related questions to pass through
# - Blocks inappropriate or non-hotel queries
# - Tripwire triggers when message should be blocked

# OUTPUT GUARDRAIL: Checks AI responses BEFORE sending to user
# - Allows appropriate hotel information to be shared
# - Blocks sensitive or inappropriate responses
# - Tripwire triggers when response should be blocked


# Create the main AI assistant agent for Hotel Hezzi
hotel_assistant_agent = Agent(
    name="Hotel Customer Care Assistant Agent",
    instructions="""You are a helpful Hotel Hezzi customer care assistant, Your name is Paul.
    - Hotel Hezzi Owner name is Mr. Huzaifa.
    - Hotel Hezzi is located in Karachi, Pakistan.
    - Hotel Hezzi has 200 rooms.
    - 25 room are for special guests not for public.
    """,
    input_guardrails=[
        input_guard_function],   # Check user messages before processing
    # Check AI responses before sending
    output_guardrails=[output_guard_function]
)


# Main conversation loop with guardrail protection
try:
    while True:
        prompt = input("User: ")

        if prompt == "exit":
            break

        # Run the AI agent with both input and output guardrails
        result = Runner.run_sync(
            starting_agent=hotel_assistant_agent, input=prompt, run_config=config)

        print(result.final_output)

# Handle guardrail tripwire exceptions
except InputGuardrailTripwireTriggered as e:
    print(f"Input Guardrail Triggered \n {e}")

except OutputGuardrailTripwireTriggered as e:
    print(f"Output Guardrail Triggered \n {e}")
