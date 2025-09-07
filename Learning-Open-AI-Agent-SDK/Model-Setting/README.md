- `temprature.py`:

  - Demonstrates `ModelSettings.temperature` (set to 0) and `top_p` (set to 1).
  - Explains how temperature controls creativity: 0 = focused/simple, ~1 = balanced, 2 = more random/creative.
  - Shows a short example that runs the agent to generate 5 creative/funny coffee-shop names.

- `presence_penalty.py`:

  - Documents `presence_penalty` (range -2.0 to 2.0): positive values encourage introducing new words/topics; negative values encourage repetition.
  - Notes `tool_choice` and `reset_tool_choice` behaviors (how the agent decides to use tools or not) and a remark about parallel tool calls requiring an API key.
  - Includes an example that runs the agent to produce a 200-word paragraph repeating the word "dragon".

- `frequency_penalty.py`:

  - Shows `frequency_penalty` (range -2.0 to 2.0) in `ModelSettings.parameters` to discourage repeated tokens and promote varied phrasing.
  - Also documents related settings: `truncation` ("auto" vs "disabled"), `max_tokens`, `reasoning` options, and `verbosity` levels.
  - Contains an example agent run similar to the temperature file (creative name generation).

- `model_setting_more_configuration.py`:
  - Lists advanced `ModelSettings` options: `store` (save prompts/output to dashboard), `include_usage`, `response_include`, and `top_logprobs`.
  - Explains `extra_query`, `extra_body`, `extra_headers`, and `extra_args` and the differences between sending parameters via URL query, request body, or SDK args.
  - Shows the `resolve()` pattern for merging base and override settings and includes a small example run.

<!-- Happy coding :) -->