# Build service layer for claims assessment
from tools.claims_tool import (get_claim_by_id,get_claim_breakup_by_claim_id)
from tools.policy_tool import get_policy_by_id
from tools.db import SessionLocal

def build_claims_context(db, claim_id):
    claim = get_claim_by_id(db, claim_id)
    if not claim:
        return None

    policy = get_policy_by_id(db, claim['policy_id'])
    breakups = get_claim_breakup_by_claim_id(db, claim_id)

    return {
        'claim': claim,
        'policy': policy,
        'breakups': breakups
    }
    
if(__name__ == '__main__'):
    db = SessionLocal()
    context = build_claims_context(db, 'CLM001')
    print(context)