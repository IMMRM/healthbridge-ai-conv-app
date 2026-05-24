from sqlalchemy.orm import Session
from models.policies import Policy


# =========================================================
# SERIALIZERS
# =========================================================
def serialize_policy(policy: Policy):
    if not policy:
        return None
    return {
        "policy_id":policy.policy_id,
        "plan_id": policy.plan_id,
        "policy_holder_id": policy.policy_holder_id,
        "sum_assured": (
            float(policy.premium)
            if policy.premium is not None else 0
        ),
        "premium": (
            float(policy.premium)
            if policy.premium is not None else 0
        ),
        "remaining_sum":(
            float(policy.remaining_sum)
            if policy.remaining_sum is not None else 0
        ),
        "start_date":(
            policy.start_date.isoformat()
            if policy.start_date else None
        ),
        "end_date":(
            policy.end_date.isoformat()
            if policy.end_date else None
        ),
        "status": policy.status
    }
    
    # =========================================================
    # Core fetch functions
    # =========================================================
def get_policy_by_id(db:Session, policy_id:str):
    policy=(db.query(Policy).filter(Policy.policy_id==policy_id).first())
    return serialize_policy(policy)

def get_policies_by_member(db:Session, member_id:str):
    policies=(db.query(Policy).filter(Policy.policy_holder_id==member_id).all())
    return [serialize_policy(policy) for policy in policies]

def get_policies_by_plan(db:Session, plan_id:str):
    policies=(db.query(Policy).filter(Policy.plan_id==plan_id).all())
    return [serialize_policy(policy) for policy in policies]

#=======================================================
# POLICY STATUS FUNCTIONS
#=======================================================

def check_policy_active(db:Session, policy_id:str):
    policy=(db.query(Policy).filter(Policy.policy_id==policy_id).first())
    if not policy:
        return False
    return policy.status=="active"

def get_remaining_sum(db:Session, policy_id:str):
    policy=(db.query(Policy).filter(Policy.policy_id==policy_id).first())
    if not policy:
        return None
    return float(policy.remaining_sum) if policy.remaining_sum is not None else 0