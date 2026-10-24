#!/usr/bin/env python3
"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""

#!/usr/bin/env python3

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

print("Step 2 complete: OpenAI client initialized!")
print(f"API key configured: {bool(os.getenv('OPENAI_API_KEY'))}")
print(f"Base URL: {os.getenv('OPENAI_API_BASE')}")


# Create marker
os.makedirs("markers", exist_ok=True)
with open("markers/task2_client_complete.txt", "w") as f:
    f.write("SUCCESS")