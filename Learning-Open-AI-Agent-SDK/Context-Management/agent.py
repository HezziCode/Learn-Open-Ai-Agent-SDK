from agents import Agent, Runner
from config import config
from tool import get_age
from dynamic_instruction import dynamic_instructions
from user_data_type_using_pydantic import UserDataType


# Context is an overloaded term Context refers to the data that the LLM does not have by default,
# and we can provide this data through various methods, such as system messages, user prompts,
# or tool schemas.



# Note about Generics:
# Generics allow us to define an Agent with a specific type of context. 
# This ensures type-safety and helps the IDE give better suggestions.



# local context represent RunContextWrapper or it can hold any normal Python object including ones 
# made with dataclasses or Pydantic.

# This part of code is called generics
user_info = UserDataType(name="Muhammad Huzaifa", age=17, role="Teacher")

assistant = Agent[UserDataType] (
    name="Assistant Agent",
    instructions=dynamic_instructions,
    tools=[get_age]
)

# Local level context! 
# -------->        -------->     -------->     -------->     -------->     -------->        -------->    
# Here we see how context is passed at the local level. Since we typed Agent with [UserDataType],
# the context must be of type UserDataType (ensuring consistency and safety).
result = Runner.run_sync(starting_agent=assistant, input="Hello", run_config=config, context=user_info)

print(result.final_output)


# 👉 If you want to know more about Generics, watch this video: 👇

#     ----->   https://www.youtube.com/watch?v=dyHV7mxT-KA&t=5583s   <-----