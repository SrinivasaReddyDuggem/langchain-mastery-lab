
from dotenv import load_dotenv
from google import genai
import os

# Step 1: Load variables from .env
load_dotenv()

# Step 2: Read API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Step 3: Verify API key exists
if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY not found. Check your .env file."
    )

# Step 4: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 5: List available models
for model in client.models.list():
    print(model.name)
