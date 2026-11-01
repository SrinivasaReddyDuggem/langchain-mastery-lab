
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from google import genai
import os
load_dotenv()
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"




api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing")

model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key,
    )

response = model.invoke("Explain REST API in one sentence.")
print(response.content)