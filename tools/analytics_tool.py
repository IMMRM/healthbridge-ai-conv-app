# tools/analytics_tool.py

from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from models.claims import Claim
from models.claims_breakup import ClaimsBreakup

from utils.serializer import serialize_model


# =========================================================
# SERIALIZATION FIELDS
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




# =========================================================
# MEMBER ANALYTICS
# =========================================================

def get_member_claim_frequency(
    db: Session,
    member_id: str
):

    count = (
        db.query(func.count(Claim.claim_id))
        .filter(Claim.member_id == member_id)
        .scalar()
    )

    return {
        "member_id": member_id,
        "total_claims": count
    }


def get_member_total_claim_amount(
    db: Session,
    member_id: str
):

    total = (
        db.query(func.sum(Claim.claim_amount))
        .filter(Claim.member_id == member_id)
        .scalar()
    )

    return {
        "member_id": member_id,
        "total_claim_amount": (
            float(total)
            if total is not None else 0
        )
    }


# =========================================================
# POLICY ANALYTICS
# =========================================================

def get_policy_total_claims(
    db: Session,
    policy_id: str
):

    count = (
        db.query(func.count(Claim.claim_id))
        .filter(Claim.policy_id == policy_id)
        .scalar()
    )

    return {
        "policy_id": policy_id,
        "total_claims": count
    }


def get_policy_total_claim_amount(
    db: Session,
    policy_id: str
):

    total = (
        db.query(func.sum(Claim.claim_amount))
        .filter(Claim.policy_id == policy_id)
        .scalar()
    )

    return {
        "policy_id": policy_id,
        "total_claim_amount": (
            float(total)
            if total is not None else 0
        )
    }


# =========================================================
# HOSPITAL ANALYTICS
# =========================================================

def get_top_hospitals_by_claims(
    db: Session,
    limit: int = 5
):

    results = (
        db.query(
            Claim.hospital_name,
            func.count(Claim.claim_id).label("claim_count")
        )
        .group_by(Claim.hospital_name)
        .order_by(desc("claim_count"))
        .limit(limit)
        .all()
    )

    return [
        {
            "hospital_name": row.hospital_name,
            "claim_count": row.claim_count
        }
        for row in results
    ]


def get_top_hospitals_by_amount(
    db: Session,
    limit: int = 5
):

    results = (
        db.query(
            Claim.hospital_name,
            func.sum(Claim.claim_amount).label("total_amount")
        )
        .group_by(Claim.hospital_name)
        .order_by(desc("total_amount"))
        .limit(limit)
        .all()
    )

    return [
        {
            "hospital_name": row.hospital_name,
            "total_claim_amount": (
                float(row.total_amount)
                if row.total_amount is not None else 0
            )
        }
        for row in results
    ]


# =========================================================
# HIGH VALUE CLAIMS
# =========================================================

def get_high_value_claims(
    db: Session,
    threshold: float = 100000
):

    claims = (
        db.query(Claim)
        .filter(Claim.claim_amount >= threshold)
        .order_by(desc(Claim.claim_amount))
        .all()
    )

    return [
        serialize_model(claim, fields=CLAIM_FIELDS)
        for claim in claims
    ]


# =========================================================
# RECENT LARGE CLAIMS
# =========================================================

def get_recent_large_claims(
    db: Session,
    limit: int = 10
):

    claims = (
        db.query(Claim)
        .order_by(desc(Claim.claim_amount))
        .limit(limit)
        .all()
    )

    return [
        serialize_model(claim, fields=CLAIM_FIELDS)
        for claim in claims
    ]


# =========================================================
# BENEFIT USAGE ANALYTICS
# =========================================================

def get_top_benefit_usage(
    db: Session,
    limit: int = 5
):

    results = (
        db.query(
            ClaimsBreakup.benefit_type,
            func.count(
                ClaimsBreakup.breakup_id
            ).label("usage_count")
        )
        .group_by(ClaimsBreakup.benefit_type)
        .order_by(desc("usage_count"))
        .limit(limit)
        .all()
    )

    return [
        {
            "benefit_type": row.benefit_type,
            "usage_count": row.usage_count
        }
        for row in results
    ]