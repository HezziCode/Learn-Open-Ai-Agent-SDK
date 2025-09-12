from agents import Agent, Runner
from agents import handoff # Use only `handoff` (singular). `handoffs` will raise an error.
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.extensions import handoff_filters
from tool import plus, weather
from config import config
from on_handoff_func_code import on_handoff_func_code, InputDataSchema



# This is handoff agent!
math_agent = Agent (
    name="Math agent",
    instructions=f""" {RECOMMENDED_PROMPT_PREFIX}
    You are a helpful Math teacher    
    """,
    tools=[plus],
    handoff_description="This is a Math teacher."
)

# Handoffs are represent as a tool to LLM
# And this is customize handoff agent!
math_agent_customization = handoff (
    agent=math_agent, # This is only required parameter in customization. 
    tool_name_override="math_teacher", # if you give space in agent/tool name override it will give an error
    tool_description_override="This is a math expert teacher.", # it will override your math agent description
    on_handoff=on_handoff_func_code, # As per docs when the handoff is triggered, this function is called first then agent will run.
    input_type=InputDataSchema, # input_type means we must pass our class name (InputDataSchema), restrict the handoff to take this data otherwise it will give error.
    input_filter=handoff_filters.remove_all_tools,  # When the main agent delegates a task, it sends full history security issue it can send tool result so its dangerous, but with ( input_filter = remove_all_tools) we can send only the relevant data needed to the specialized agent.
    is_enabled=True # This is powerful parameter you can add your on logic to enable or disable the handoff like if user paid fees then he can use your tool otherwise not.
)


# Handoffs are represent as a tool to LLM
assistant_agent = Agent (
    name="Assistant Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful assistant""",

    handoff_description="You are a helpful assistant agent your work is to delegate task to specialize agent",
    handoffs=[math_agent_customization],
    tools=[weather]
)

info = {"name": "Huzaifa", "age": 17, "role": "student"}

result = Runner.run_sync(starting_agent = assistant_agent, input="Tell me about karachi weather and what is 2+2?", run_config=config, context=info)

print(result.last_agent.name)
print(result.final_output)