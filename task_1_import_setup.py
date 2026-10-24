#!/usr/bin/env python3
# Task 1: Import Required Libraries
# Learn what libraries we need for AI API calls.

# Step 1: Import the OpenAI library
# This library helps us talk to AI models
import openai

# Step 2: Import os for environment variables
# This helps us access API keys safely
import os

print("Step 1 complete: Libraries imported!")
print(f"OpenAI SDK version: {openai.__version__}")

# Create marker
os.makedirs("markers", exist_ok=True)
with open("markers/task1_imports_complete.txt", "w") as f:
    f.write("SUCCESS")
