# Simple Guide: Contexts, Run Context, and Tools (for everyone)

This guide explains, in a simple and friendly way, the main ideas in this project:

## Quick idea: What is context?

- Imagine you have a friend who asks questions. "Context" is the little story or facts you give your friend so they can answer better.
- Example: If you say "My name is Ani and I am 7", this helps your friend know who you are.

## Two kinds of context in this project

1. LLM context (what we send to the AI)
   - This is the information we share with the language model (LLM) when we ask it to do something.
   - It helps the LLM understand the current user or situation.
2. Local context (what our code keeps)
   - This is the data stored inside the program while it runs.
   - It might be the same as LLM context or include extra details we don't send to the LLM.

Both types are plain facts like `name`, `age`, and `role`.

## Run context: a simple wrapper for passing context

- In code, we use something called `RunContextWrapper` to wrap the user's data and pass it into tools (small helper functions).
- Think of `RunContextWrapper` as a small box that carries the user's facts to the tool.

Example of what's inside the box (the user data type):

- `name` (text)
- `age` (number)
- `role` (text)

These fields are defined in two similar ways in the project:

- `user_data_type_using_pydantic.py` uses Pydantic:
  - class `UserDataType(BaseModel)` with `name`, `age`, `role` fields.
- `user_data_type_using_dataclasses.py` uses dataclasses:
  - `@dataclass class UserDataType` with the same fields.

Both are just different ways for Python to represent the same kind of data.

## Why two ways (Pydantic vs Dataclass)?

- Dataclasses are simple and built into Python. They are like plain boxes to store data.
- Pydantic adds validation and makes sure the data types are correct (for example, `age` really is a number). It's a bit safer.

For beginners: both store `name`, `age`, and `role`. Use dataclasses if you want simple code. Use Pydantic if you want automatic checks.

## Generics: a short, friendly note

- The code uses a generic wrapper `RunContextWrapper[UserDataType]`. "Generic" means the wrapper can carry any kind of user data. Imagine a backpack that can hold different toys.
- Here the backpack holds `UserDataType` (name, age, role).

## Dynamic instructions (what are they?)

- Dynamic instructions are short messages or rules we can change while the program runs.
- Example: we might tell the LLM "Always answer simply" or "Use friendly tone". These instructions can be updated on the fly.
- They help the AI behave the way we want for a specific situation.

## Tools and `get_age` example (what the tool does)

- A "tool" here is a small function that does one job and can read the run context.
- Look at `tool.py`. There is a function `get_age` that gets the run context:
  - It receives `ctx: RunContextWrapper[UserDataType]`.
  - It prints the role and returns a string like `I am 25` using `ctx.context.age`.

Simple explanation: the tool opens the box (run context), looks at the `age` inside, and says it out loud.

## How the code shares context with the LLM

- The program can take a few fields (for example, only `age`) and send them to the LLM using a function tool call. That way the LLM only sees what we want it to see.
- This is useful for privacy and for keeping the AI focused.

## Very small walkthrough for beginners

1. Open the project files.
2. See `user_data_type_using_dataclasses.py` or `user_data_type_using_pydantic.py` to understand the fields (`name`, `age`, `role`).
3. `tool.py` has the `get_age` function. It receives `RunContextWrapper[UserDataType]` and uses `ctx.context.age`.
4. When the program runs, it can choose which parts of the user data to send to the LLM (LLM context) and what it keeps locally (local context).

## Why this matters (short)

- Keeping local context and carefully choosing LLM context helps with safety and clarity.
- Dynamic instructions and typed user data make the assistant behave predictably.

## Final friendly note

This project shows simple ideas: store user facts (name, age, role), wrap them in a `RunContextWrapper`, and let small tools (like `get_age`) read them. Use dataclasses for simplicity or Pydantic for extra safety. Change instructions on the fly with dynamic instructions to guide the AI's behavior.

If you want, I can make this README even shorter into a one-page explanation for 5-year-olds with pictures and examples—tell me which style you prefer.
