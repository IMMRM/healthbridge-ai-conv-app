# services/claim_assessment_service.py

from tools.claims_tool import (
    get_claim_by_id,
    get_claim_breakup_by_claim_id
)

from tools.policy_tool import (
    get_policy_by_id
)

from tools.member_tool import (
    get_member_by_id
)

from tools.benefits_tool import (
    get_plan_benefits
)


def build_claim_context(
    db,
    claim_id: str
):

    # ============================================
    # CLAIM
    # ============================================

    claim = get_claim_by_id(
        db,
        claim_id
    )

    if not claim:
        return None

    # ============================================
    # POLICY
    # ============================================

    policy = get_policy_by_id(
        db,
        claim["policy_id"]
    )

    # ============================================
    # MEMBER
    # ============================================

    member = get_member_by_id(
        db,
        claim["member_id"]
    )

    # ============================================
    # CLAIM BREAKUP
    # ============================================

    breakups = get_claim_breakup_by_claim_id(
        db,
        claim_id
    )

    # ============================================
    # BENEFITS
    # ============================================

    benefits = []

    if policy:

        benefits = get_plan_benefits(
            db,
            policy["plan_id"]
        )

    # ============================================
    # FINAL CONTEXT
    # ============================================

    return {
        "claim": claim,
        "policy": policy,
        "member": member,
        "benefits": benefits,
        "claim_breakups": breakups
    }


if __name__ == "__main__":

    from tools.db import SessionLocal

    db = SessionLocal()

    context = build_claim_context(
        db,
        "CLM001"
    )

    print(context)

    db.close()