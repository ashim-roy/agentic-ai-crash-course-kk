
import json
from llm_client import client

# Actual Python functions the application is allowed to execute.
def calculate_sum(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def calculate_product(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# Allowlist: maps tool names requested by the model to Python functions.
tool_registry = {
    "calculate_sum": calculate_sum,
    "calculate_product": calculate_product,
}

# Tool schemas tell the model each function's name and required arguments.
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_sum",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_product",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]

messages = [
    {
        "role": "system",
        "content": (
            "You are a calculator assistant. For multi-step calculations, "
            "use the actual result returned by each tool in subsequent steps. "
            "Never invent a tool result."
        ),
    },
    {
        "role": "user",
        "content": "Calculate 12 multiplied by 8, then add 4 to that result.",
    },
]

MAX_ROUNDS = 5  # Prevents the agent from calling tools indefinitely.

for round_number in range(MAX_ROUNDS):
    # Ask the model to either call a tool or provide its final answer.
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message

    # Preserve the assistant message, including any tool-call requests.
    messages.append(message)

    # No tool calls means the model has finished with a text answer.
    if not message.tool_calls:
        print("\nFinal answer:")
        print(message.content)
        break

    # Execute every tool requested in this round.
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        # Never execute an unknown function.
        if name not in tool_registry:
            raise ValueError(f"Unsupported tool: {name}")

        # Run the selected Python function with the supplied arguments.
        result = tool_registry[name](**args)
        print(f"Round {round_number + 1}: {name}({args}) = {result}")

        # Send the result back, linked to the original tool-call ID.
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result),
        })
else:
    # The loop ended without receiving a final text response.
    raise RuntimeError("Agent reached the maximum number of rounds.")
