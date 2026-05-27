# claims_tool.py

from sqlalchemy.orm import Session
from sqlalchemy import desc
from utils.serializer import serialize_model

from models.claims import Claim
from models.claims_breakup import ClaimsBreakup


# =========================================================
# CLAIMS FIELDS
# =========================================================
CLAIM_FIELDS = [
    "claim_id",
    "policy_id",
    "member_id",
    "claim_date",
    "claim_amount",
    "approved_amount",
    "status",
    "hospital_name",
    "claim_type"
]

# ========================================================
# CLAIMS BREAKUP FIELDS
# ========================================================
CLAIM_BREAKUP_FIELDS = [
    "breakup_id",
    "claim_id",
    "benefit_type",
    "sub_type",
    "amount",
    "approved_amount",
    "remarks"
]

# =========================================================
# SERIALIZERS
# =========================================================

# def serialize_claim(claim: Claim):

#     if not claim:
#         return None

#     return serialize_model(claim, CLAIM_FIELDS)
        

# def serialize_claim_breakup(breakup: ClaimsBreakup):

#     return serialize_model(breakup, CLAIM_BREAKUP_FIELDS)
    


# =========================================================
# CORE FETCH FUNCTIONS
# =========================================================

def get_claim_by_id(
    db: Session,
    claim_id: str
):

    claim = (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )

    return serialize_model(claim,CLAIM_FIELDS)


def get_claim_breakup_by_claim_id(
    db: Session,
    claim_id: str
):

    breakups = (
        db.query(ClaimsBreakup)
        .filter(ClaimsBreakup.claim_id == claim_id)
        .all()
    )

    return [
        serialize_model(b, CLAIM_BREAKUP_FIELDS)
        for b in breakups
    ]


# =========================================================
# CLAIM HISTORY FUNCTIONS
# =========================================================

def get_claims_by_member_id(
    db: Session,
    member_id: str
):

    claims = (
        db.query(Claim)
        .filter(Claim.member_id == member_id)
        .order_by(desc(Claim.claim_date))
        .all()
    )

    return [
        serialize_model(claim, CLAIM_FIELDS)
        for claim in claims
    ]


def get_claims_by_policy_id(
    db: Session,
    policy_id: str
):

    claims = (
        db.query(Claim)
        .filter(Claim.policy_id == policy_id)
        .order_by(desc(Claim.claim_date))
        .all()
    )

    return [
        serialize_model(claim, CLAIM_FIELDS)
        for claim in claims
    ]


def get_recent_claims(
    db: Session,
    limit: int = 10
):

    claims = (
        db.query(Claim)
        .order_by(desc(Claim.claim_date))
        .limit(limit)
        .all()
    )

    return [
        serialize_model(claim, CLAIM_FIELDS)
        for claim in claims
    ]


# =========================================================
# UPDATE FUNCTIONS
# =========================================================

def update_claim_status(
    db: Session,
    claim_id: str,
    new_status: str
):

    claim = (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )

    if not claim:
        return None

    claim.status = new_status

    db.commit()
    db.refresh(claim)

    return serialize_model(claim, CLAIM_FIELDS)


# =========================================================
# CREATE CLAIM
# =========================================================

def create_claim(
    db: Session,
    claim_data: dict
):

    new_claim = Claim(**claim_data)

    db.add(new_claim)

    db.commit()

    db.refresh(new_claim)

    return serialize_model(new_claim, CLAIM_FIELDS)