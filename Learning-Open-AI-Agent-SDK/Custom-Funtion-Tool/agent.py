from agents import Agent, Runner,  RunContextWrapper, GuardrailFunctionOutput
from agents.guardrail import output_guardrail
from tool import addition, subtraction, multiply
from config import config



@output_guardrail(name="force_tool_usage")
async def enforce_tool(ctx: RunContextWrapper, agent: Agent, agent_output: str) -> GuardrailFunctionOutput:
    """
    If the LLM answers on its own (skipping the tool), trigger the tripwire.
    If the output comes from a tool, do not trigger the tripwire.
    """
    # Check if model answered directly with a number or math result
    looks_like_direct_math = agent_output.strip().isdigit()

    return GuardrailFunctionOutput(
        output_info={},
        tripwire_triggered=looks_like_direct_math
    )



assistant_agent = Agent(
    name="Assistant Agent",
    instructions="""Always use tools for math. Never calculate directly

- For addition: use addition tool
- For subtraction: use subtraction tool  
- For multiplication: use multiply tool

Do not show tool code in your response.
Do not show any code examples or function calls in your response.
If tools are disabled, only show the error message.""",
    tools=[addition, subtraction, multiply],
    output_guardrails=[enforce_tool]
)


# This part check the things in terminal that is mention their 👇

# for tool in assistant_agent.tools:
#     if isinstance(tool, FunctionTool):
#         print(tool.name)
#         print(tool.description)
#         print(json.dumps(tool.params_json_schema, indent=2))
#         print()


# Get user information first
name = input("Enter your name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")

info = {"name": name, "age": age, "role": role}



prompt = input("Enter your quries: ")
try:
    result = Runner.run_sync(
        starting_agent=assistant_agent,
        input=prompt,
        run_config=config,
        context=info
    )
    print(result.final_output)
except Exception:
    print("Sorry, tools are not accessible because you are under 18.")