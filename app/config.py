import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_cheap_llm():
    return ChatOpenAI(
        base_url=os.getenv("BASE_URL"),
        api_key=os.getenv("GROQ_API_KEY"),
        model=os.getenv("MODEL_NAME"),
        temperature=0.9  # important for varied greetings
    )