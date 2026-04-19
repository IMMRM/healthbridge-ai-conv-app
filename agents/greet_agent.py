from langchain_core.prompts import PromptTemplate
from app.config import get_cheap_llm
from llm.prompts import GREET_PROMPT

def greet_user(user_input: str) -> str:
    llm = get_cheap_llm()

    prompt = PromptTemplate.from_template(GREET_PROMPT)

    chain = prompt | llm

    response = chain.invoke({"input": user_input})
    return response.content