
import json
from llm_client import client

def calculate_sum(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_sum",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "Calculate 125 + 375 using the calculator and explain the result."
    }
]

# Step 1: Ask the model what to do.
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# Step 2: Add the assistant's response to conversation history.
messages.append(message)

# Step 3: Execute each requested tool.
if message.tool_calls:
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        if name == "calculate_sum":
            result = calculate_sum(**args)
        else:
            raise ValueError(f"Unknown tool: {name}")

        print(f"Tool result: {result}")

        # Step 4: Send the tool result back to the model.
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })

    # Step 5: Ask the model to produce the final answer.
    final_response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    print("\nFinal answer:")
    print(final_response.choices[0].message.content)
else:
    print(message.content)
