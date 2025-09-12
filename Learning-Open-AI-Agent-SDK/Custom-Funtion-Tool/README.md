# Custom Function Tools with OpenAI Agent SDK


🎥 **Watch this video first to understand the logic and this code:**  
👉 [I Built Function Tools with Business Logic ](https://www.youtube.com/watch?v=mTBYQBbUhQg)



This project demonstrates advanced custom function tool implementation using the OpenAI Agent SDK, showcasing various features like tool validation, output guardrails, error handling, and conditional tool enabling.

## 🚀 Key Features Covered

### 1. **Custom Function Tools**

- **Function Tool Decorator**: Using `@function_tool` decorator for simple tool creation
- **Manual FunctionTool Class**: Creating tools with `FunctionTool` class for advanced control
- **Tool Schema Integration**: Using Pydantic models for parameter validation

### 2. **Tool Enabling/Disabling (`is_enabled` Parameter)**

- **Conditional Tool Access**: Tools can be enabled/disabled based on user context
- **Age-Based Validation**: Example implementation restricting tool access for users under 18
- **Dynamic Tool Control**: Runtime evaluation of tool availability

### 3. **Failure Error Handling**

- **Custom Error Functions**: Implementing `failure_error_function` for graceful error handling
- **Error Masking**: Converting internal errors to user-friendly messages
- **Exception Management**: Proper error handling and logging

### 4. **Output Guardrails**

- **Tool Usage Enforcement**: Ensuring AI uses tools instead of direct calculations
- **Tripwire Mechanism**: Detecting and preventing unwanted AI behavior
- **Response Validation**: Validating AI outputs before returning to user

### 5. **Advanced Tool Configuration**

- **Name Override**: Custom tool names using `name_override`
- **Description Override**: Custom descriptions using `description_override`
- **Parameter Schema**: JSON schema generation from Pydantic models
- **Context Wrapper**: Accessing user context within tools


### 1. Function Tool Decorator Approach

```python
@function_tool(is_enabled=tool_validation)
def addition(n1: int, n2: int) -> str:
    """Addition tool with automatic schema generation"""
    return f"Your answer is {n1+n2}"
```

### 2. Manual FunctionTool Class Approach

```python
subtraction = FunctionTool(
    name="subtract",
    description="This is subtract tool",
    params_json_schema=tool_schema.model_json_schema(),
    on_invoke_tool=subtract_function,
    is_enabled=tool_validation
)
```

### 3. Advanced Tool with Error Handling

```python
@function_tool(
    name_override="multiply_tool",
    description_override="This is multiply tool function",
    is_enabled=tool_validation,
    failure_error_function=my_custom_error_function
)
def multiply(n1: int, n2: int) -> str:
    """Multiply tool with custom error handling"""
    return f"Your answer is {n1*n2}"
```

## 🔒 Tool Validation System

### Age-Based Access Control

```python
async def tool_validation(ctx: RunContextWrapper[UserDataType], agent: Agent[UserDataType]):
    """Enable tools only for users 18 and older"""
    if ctx.context["age"] >= 18:
        return True
    else:
        return False
```

### User Context Integration

- **Typed Context**: Using Pydantic models for strong typing
- **Runtime Validation**: Dynamic tool enabling based on user data
- **Secure Access**: Preventing unauthorized tool usage

## 🛡️ Output Guardrails

### Tool Usage Enforcement

```python
@output_guardrail(name="force_tool_usage")
async def enforce_tool(ctx: RunContextWrapper, agent: Agent, agent_output: str) -> GuardrailFunctionOutput:
    """Prevent AI from answering directly without using tools"""
    looks_like_direct_math = agent_output.strip().isdigit()

    return GuardrailFunctionOutput(
        output_info={},
        tripwire_triggered=looks_like_direct_math
    )
```

### Guardrail Features

- **Response Monitoring**: Analyzing AI outputs for compliance
- **Tripwire System**: Triggering alerts for policy violations
- **Behavior Control**: Enforcing specific AI behavior patterns

## ⚠️ Error Handling

### Custom Error Functions

```python
def my_custom_error_function(context: RunContextWrapper[Any], error: Exception) -> str:
    """Convert internal errors to user-friendly messages"""
    print(f"A tool call failed with the following error: {error}")
    return "An internal server error occurred. Please try again later."
```

### Error Handling Benefits

- **User Experience**: Friendly error messages instead of technical details
- **Security**: Preventing information leakage through error messages
- **Logging**: Proper error tracking for debugging

## 📋 Schema Validation

### Pydantic Integration

```python
class tool_schema(BaseModel):
    n1: int
    n2: int

class UserDataType(BaseModel):
    name: str
    age: int
    role: str
```

### Schema Benefits

- **Type Safety**: Automatic parameter validation
- **JSON Schema**: Auto-generation for LLM integration
- **Documentation**: Self-documenting parameter requirements

## 🎯 Use Cases

1. **Restricted Access Systems**: Age-based or role-based tool access
2. **Financial Applications**: Secure calculation tools with validation
3. **Educational Platforms**: Controlled AI assistance with guardrails
4. **Enterprise Solutions**: Error handling and audit trails
5. **API Integrations**: Robust tool calling with fallback mechanisms

## 🔧 Key Concepts Demonstrated

- **Tool Lifecycle Management**: Enable/disable tools dynamically
- **Context-Aware Tools**: Access user data within tool functions
- **Error Resilience**: Graceful handling of tool failures
- **AI Behavior Control**: Using guardrails to enforce policies
- **Type Safety**: Strong typing with Pydantic models
- **Flexible Configuration**: Override names, descriptions, and behaviors

## 💡 Best Practices Shown

1. **Always validate inputs** using Pydantic schemas
2. **Implement proper error handling** for production readiness
3. **Use guardrails** to control AI behavior
4. **Enable/disable tools** based on user context
5. **Provide clear tool descriptions** for better AI understanding
6. **Log errors** while showing user-friendly messages

## 🔍 How It Works

### Tool Execution Flow

1. **User Input**: User provides name, age, role, and query
2. **Context Validation**: System checks if user meets tool access criteria
3. **Tool Enabling**: Tools are enabled/disabled based on validation results
4. **AI Processing**: Agent processes query and attempts to use appropriate tools
5. **Guardrail Check**: Output guardrails validate AI response
6. **Error Handling**: Any tool failures are caught and handled gracefully
7. **Final Output**: User receives either tool result or appropriate error message

### Security Features

- **Age Verification**: Tools only accessible to users 18+
- **Error Masking**: Internal errors converted to safe messages
- **Behavior Enforcement**: AI forced to use tools instead of direct calculation
- **Context Isolation**: User data properly typed and validated

This implementation showcases a production-ready approach to custom function tools with comprehensive error handling, validation, and security features.

<!-- I think this is enough :) too much for today -->
<!-- Happy coding -->