
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load API configuration from .env

# Create one reusable OpenAI client.
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE") or "https://api.openai.com/v1"
)

def ask_llm(prompt: str) -> str:
    """Send a prompt to the model and return its text response."""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content or ""
    # Return only the generated text, not the entire response object.
