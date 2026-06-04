from sqlalchemy.orm import Session
from models.policies import Policy
from utils.serializer import serialize_model

# =========================================================
# POLICY FIELDS
# =========================================================
POLICY_FIELDS = [
    "policy_id",
    "plan_id",
    "policy_holder_id",
    "sum_assured",
    "premium",
    "remaining_sum",
    "start_date",
    "end_date",
    "status"
]

    # =========================================================
    # Core fetch functions
    # =========================================================
def get_policy_by_id(db:Session, policy_id:str):
    policy=(db.query(Policy).filter(Policy.policy_id==policy_id).first())
    return serialize_model(policy, POLICY_FIELDS)

def get_policies_by_member(db:Session, member_id:str):
    policies=(db.query(Policy).filter(Policy.policy_holder_id==member_id).all())
    return [serialize_model(policy, POLICY_FIELDS) for policy in policies]

def get_policies_by_plan(db:Session, plan_id:str):
    policies=(db.query(Policy).filter(Policy.plan_id==plan_id).all())
    return [serialize_model(policy, POLICY_FIELDS) for policy in policies]

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