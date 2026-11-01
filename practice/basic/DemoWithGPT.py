
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import os
load_dotenv()
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

api_key = os.getenv("OPENROUTER_API_KEY")
model = ChatOpenAI(
        model="openai/gpt-4o-mini",
        base_url=OPENROUTER_BASE_URL,
        api_key=api_key,
    )

response = model.invoke("Explain REST API in one sentence.")
print(response.content)