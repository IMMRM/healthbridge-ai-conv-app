import os

from dotenv import load_dotenv

from tools.db import SessionLocal

from agents.claims_assessment_agent import (
    ClaimAssessmentAgent
)

load_dotenv()

db = SessionLocal()

agent = ClaimAssessmentAgent(
    db=db,
    model_name=os.getenv("MODEL_NAME"),
    groq_api_key=os.getenv("GROQ_API_KEY")
)

response = agent.assess_claim(
    claim_id="CLM001",
    question="Give me information about my claim"
)

print(response)

db.close()
