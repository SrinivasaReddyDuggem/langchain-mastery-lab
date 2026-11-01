import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

nativeOpenRouterModel = init_chat_model(
    model="openai/gpt-4o-mini",
    model_provider="openrouter",
    temperature=0.7,
)

nativeOpenRouterResponse = nativeOpenRouterModel.invoke(
    "What is langchain and how is it used in AI applications?"
)

print("Native OpenRouter Response =====", nativeOpenRouterResponse.content)


openRouterModel = init_chat_model(
    "openai/gpt-4o-mini",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

openRouterResponse = openRouterModel.invoke(
    "Explain what a LLM is."
)

print("open Router Response =====  ",openRouterResponse.content)



