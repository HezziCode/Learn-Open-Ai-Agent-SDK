# Hotel Hezzi AI Assistant with Guardrails 🏨🤖

## What is this project?

This is an AI-powered customer service assistant for Hotel Hezzi that uses **Guardrails** to ensure safe and appropriate conversations. Think of it like having a smart receptionist that can answer questions about the hotel, but with built-in safety features.

## What are Guardrails? 🛡️

**Guardrails** are like security guards for AI conversations. They check messages before and after the AI processes them to make sure everything is safe and appropriate.

Imagine guardrails as:

- 🚪 **Bouncers at a club** - they check who can enter
- 🔍 **Quality inspectors** - they check what comes out
- ⚠️ **Warning systems** - they alert when something is wrong

## Types of Guardrails

### 1. Input Guardrails (Before AI Processing) 📥

**What it does:** Checks user messages BEFORE the AI assistant sees them.

**Example:**

```
User asks: "How many rooms does Hotel Hezzi have?"
Input Guardrail: ✅ "This is a valid hotel question - ALLOW"
AI Assistant: "Hotel Hezzi has 200 rooms available."
```

```
User asks: "How to hack into hotel systems?"
Input Guardrail: ❌ "This is inappropriate - BLOCK"
Result: Message blocked, AI never sees it
```

**Tripwire Parameter:**

- `tripwire_triggered = True` → Block the message
- `tripwire_triggered = False` → Allow the message

### 2. Output Guardrails (After AI Processing) 📤

**What it does:** Checks AI responses BEFORE sending them to the user.

**Example:**

```
AI wants to say: "Hotel Hezzi has 200 rooms, 25 are for special guests."
Output Guardrail: ✅ "This response is appropriate - ALLOW"
User sees: "Hotel Hezzi has 200 rooms, 25 are for special guests."
```

```
AI wants to say: "Here's the hotel's private security codes..."
Output Guardrail: ❌ "This contains sensitive info - BLOCK"
User sees: "I cannot share sensitive security information."
```

**Tripwire Parameter:**

- `tripwire_triggered = True` → Block the AI response
- `tripwire_triggered = False` → Allow the AI response

## How the Code Works 💻

### Simple Flow:

1. **User types message** → Input Guardrail checks it
2. **If safe** → AI Assistant processes it
3. **AI generates response** → Output Guardrail checks it
4. **If safe** → User sees the response

### Code Structure:

```python
# Input Guardrail checks user messages
@input_guardrail
async def input_guard_function(ctx, agent, input):
    # Check if message is about hotel
    result = check_message(input)
    return GuardrailFunctionOutput(
        tripwire_triggered=not result.is_hotel_query  # Block non-hotel questions
    )

# Output Guardrail checks AI responses
@output_guardrail
async def output_guard_function(ctx, agent, output):
    # Check if response is safe to share
    result = check_response(output)
    return GuardrailFunctionOutput(
        tripwire_triggered=result.contains_sensitive_info  # Block sensitive info
    )
```

## Real-World Example 🌟

**Scenario:** Customer asks about room availability in Urdu

```
User: "Hezzi hotel mein kitne rooms hain?"
↓
Input Guardrail: "This is about Hotel Hezzi ✅ - Allow"
↓
AI Assistant: "Hotel Hezzi has 200 rooms available in Karachi, Pakistan."
↓
Output Guardrail: "Response is appropriate ✅ - Allow"
↓
User sees: "Hotel Hezzi has 200 rooms available in Karachi, Pakistan."
```

## Why Use Guardrails? 🤔

1. **Safety First:** Prevents inappropriate conversations
2. **Brand Protection:** Ensures AI stays on-topic (hotel-related)
3. **Privacy Protection:** Blocks sharing of sensitive information
4. **Quality Control:** Maintains professional customer service standards


_This system ensures that Hotel Hezzi's AI assistant provides helpful, safe, and appropriate customer service while protecting both customers and the hotel's interests._
