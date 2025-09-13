from agents import Agent, Runner, SQLiteSession
from config import config
import asyncio

assistant_agent = Agent (
    name="Assistant Agent",
    instructions="You are a helpful assistant"
)








# LLM are stateless, so we need to store the conversation history.

# conversation.db stores chats; user1 = person1 messages. Change to user2 for a new conversation.

session_history = SQLiteSession("user1", "conversion.db")



# Clear the session history means clear your database
# async def main():
#     await session_history.clear_session()
# asyncio.run(main())

while True:
    prompt = input("User: ")

    if prompt == "exit":
        break

    result = Runner.run_sync(starting_agent = assistant_agent, input=prompt, session=session_history, run_config=config)

    print(result.last_agent.name)

    print(result.final_output)