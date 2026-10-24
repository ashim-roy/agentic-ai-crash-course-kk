
import json
from llm_client import client

# Define a tool the model is allowed to request.
def calculate_sum(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

# Describe the tool to the model using a JSON schema.
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_sum",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

# Ask the model to solve a problem, providing the available tool.
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": "What is 125 plus 375? Use the calculator tool."}
    ],
    tools=tools,
    tool_choice="auto"
)

# Inspect whether the model requested a tool.
message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        # Extract the requested function name and its JSON arguments.
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        # Execute the function in our Python application.
        if function_name == "calculate_sum":
            result = calculate_sum(**arguments)
            print(f"Tool requested: {function_name}")
            print(f"Arguments: {arguments}")
            print(f"Python tool result: {result}")
else:
    print(message.content)
