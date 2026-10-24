
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Loads API configuration from your .env file.

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # Reads the API key for authentication.
    base_url=os.getenv("OPENAI_API_BASE") or "https://api.openai.com/v1"
    # Uses your configured API endpoint or the official OpenAI endpoint.
)

prompt = "Explain the benefits of using AI for customer support in a business"
# Stores the input prompt so we can send it and understand its token usage.

response = client.chat.completions.create(
    model="gpt-4.1-mini",  # Selects the model to generate the answer.
    messages=[{"role": "user", "content": prompt}]  # Sends the user prompt.
)

input_tokens = response.usage.prompt_tokens
# Number of tokens used by the input, including applicable message formatting.

output_tokens = response.usage.completion_tokens
# Number of tokens generated in the model's response.

total_tokens = response.usage.total_tokens
# Total tokens reported for this request (input + output).

print(f"Input tokens:  {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Total tokens:  {total_tokens}")

# Example GPT-4.1 mini rates in USD per 1,000,000 tokens.
# Verify current pricing before using these figures for budgeting.
input_price_per_million = 0.40
output_price_per_million = 1.60

input_cost = input_tokens / 1_000_000 * input_price_per_million
# Estimates input cost by multiplying input tokens by the input rate.

output_cost = output_tokens / 1_000_000 * output_price_per_million
# Estimates output cost separately because input and output rates differ.

total_cost = input_cost + output_cost
# Adds both estimates to calculate the approximate request cost.

print(f"\nEstimated input cost:  ${input_cost:.8f}")
print(f"Estimated output cost: ${output_cost:.8f}")
print(f"Estimated total cost:  ${total_cost:.8f}")

os.makedirs("markers", exist_ok=True)
# Ensures the local directory exists for course progress markers.

with open("markers/task5_costs_complete.txt", "w") as f:
    f.write("SUCCESS")  # Records that the script reached the end.
