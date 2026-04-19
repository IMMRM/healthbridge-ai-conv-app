from langchain_core.prompts import PromptTemplate
from app.config import get_cheap_llm
from agents.greet_agent import greet_user
from agents.fallback_agent import fallback_response
from llm.prompts import ROUTER_PROMPT


def classify_intent(user_input: str) -> str:
    llm = get_cheap_llm()

    prompt = PromptTemplate.from_template(ROUTER_PROMPT)

    chain = prompt | llm

    response = chain.invoke({"input": user_input})

    intent = response.content.strip().lower()

    return intent


def route_query(user_input: str) -> str:
    intent = classify_intent(user_input)

    print(f"[Router] Detected intent: {intent}")  # for debugging

    # Based on the intent, we need to call that particular agent
    if intent == "greeting":
        return greet_user(user_input)

    return fallback_response(user_input)