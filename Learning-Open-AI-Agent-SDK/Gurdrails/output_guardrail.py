from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner, output_guardrail, TResponseInputItem
from config import config
from schema_pydantic import Output_guardrail_schema

output_guardrail_agent = Agent(
    name="Output Guardrail",
    instructions="You are an output guardrail, Check hotel Hezzi quires regarding tax or hotel core details like monthly sales or whatever is imp it is.",
    output_type=Output_guardrail_schema
)

@output_guardrail
async def output_guard_function(ctx:RunContextWrapper[None], agent:Agent, input: str | list [TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, input=input, run_config=config, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_Hezzi_account_tax_details
    )