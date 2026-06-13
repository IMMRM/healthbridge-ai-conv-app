import json

from langchain_groq import ChatGroq

from llm.prompts.claims_assessment_prompt import (
    CLAIM_ASSESSMENT_PROMPT
)

from services.claims_assessment_service import (
    build_claim_context
)


class ClaimAssessmentAgent:

    def __init__(
        self,
        db,
        model_name: str,
        groq_api_key: str
    ):

        self.db = db

        self.llm = ChatGroq(
            model=model_name,
            api_key=groq_api_key,
            temperature=0
        )

        self.chain = (
            CLAIM_ASSESSMENT_PROMPT
            | self.llm
        )

    def assess_claim(
        self,
        claim_id: str,
        question: str
    ):

        context = build_claim_context(
            self.db,
            claim_id
        )

        if not context:
            return (
                f"Claim {claim_id} not found."
            )

        response = self.chain.invoke(
            {
                "question": question,
                "context": json.dumps(
                    context,
                    indent=2
                )
            }
        )

        return response.content