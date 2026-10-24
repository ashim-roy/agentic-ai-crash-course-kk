
#!/usr/bin/env python3
# Tells Unix-like systems to use Python 3 when executing this script.

import os
# Provides access to environment variables and filesystem operations.

from dotenv import load_dotenv
# Imports the helper that loads configuration from a .env file.

from openai import OpenAI
# Imports the OpenAI client class directly from the OpenAI SDK.
# This is an alternative to importing the entire `openai` module.

load_dotenv()
# Loads OPENAI_API_KEY and any other configured variables from .env.

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    # Reads the API key from the environment for authentication.

    base_url=os.getenv("OPENAI_API_BASE") or "https://api.openai.com/v1"
    # Uses the configured API endpoint, falling back to the official
    # OpenAI endpoint when OPENAI_API_BASE is unset or empty.
)

# Make a new API request.
response = client.chat.completions.create(
    # Calls the Chat Completions API using the initialized client.

    model="gpt-4.1-mini",
    # Selects the language model to answer the question.

    messages=[
        # Sends the conversation as a list of message dictionaries.

        {
            "role": "user",
            # Marks the message as user input.

            "content": "What is Python in one sentence?"
            # The prompt that the model will answer.
        }
    ]
)
# The returned response object contains the model's answer and metadata.

# Extract the AI-generated text.
ai_text = response.choices[0].message.content
# response        -> the complete API response object
# .choices        -> the list of generated choices
# [0]             -> the first choice
# .message        -> the message for that choice
# .content        -> the actual generated text
#
# Result: ai_text is a string containing the answer.

print("AI's Answer:")
# Prints a heading to make the terminal output easier to read.

print(ai_text)
# Prints only the extracted answer, not the entire response object.

os.makedirs("markers", exist_ok=True)
# Creates the markers directory if it doesn't already exist.

with open("markers/task4_extract_complete.txt", "w") as f:
    # Creates or overwrites the marker file and ensures it is closed.

    f.write("SUCCESS")
    # Records that the script reached the completion step.
