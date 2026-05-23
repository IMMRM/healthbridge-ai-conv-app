# claims_tool.py

from sqlalchemy.orm import Session
from sqlalchemy import desc

from models.claims import Claim
from models.claims_breakup import ClaimsBreakup


# =========================================================
# SERIALIZERS
# =========================================================

def serialize_claim(claim: Claim):

    if not claim:
        return None

    return {
        "claim_id": claim.claim_id,
        "policy_id": claim.policy_id,
        "member_id": claim.member_id,
        "claim_date": (
            claim.claim_date.isoformat()
            if claim.claim_date else None
        ),
        "claim_amount": (
            float(claim.claim_amount)
            if claim.claim_amount is not None else 0
        ),
        "approved_amount": (
            float(claim.approved_amount)
            if claim.approved_amount is not None else 0
        ),
        "status": claim.status,
        "hospital_name": claim.hospital_name,
        "claim_type": claim.claim_type
    }


def serialize_claim_breakup(breakup: ClaimsBreakup):

    return {
        "breakup_id": breakup.breakup_id,
        "claim_id": breakup.claim_id,
        "benefit_type": breakup.benefit_type,
        "sub_type": breakup.sub_type,
        "amount": (
            float(breakup.amount)
            if breakup.amount is not None else 0
        ),
        "approved_amount": (
            float(breakup.approved_amount)
            if breakup.approved_amount is not None else 0
        ),
        "remarks": breakup.remarks
    }


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

    return serialize_claim(claim)


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
        serialize_claim_breakup(b)
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
        serialize_claim(claim)
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
        serialize_claim(claim)
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
        serialize_claim(claim)
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

    return serialize_claim(claim)


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

    return serialize_claim(new_claim)