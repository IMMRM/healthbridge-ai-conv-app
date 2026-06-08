from sqlalchemy.orm import Session

from models.plan_benefits import PlanBenefit

from utils.serializer import serialize_model


# =========================================================
# SERIALIZATION FIELDS
# =========================================================

BENEFIT_FIELDS = [
    "benefit_id",
    "plan_id",
    "benefit_type",
    "sub_type",
    "coverage_limit",
    "waiting_period",
    "is_covered",
    "remarks"
]


# =========================================================
# SERIALIZERS
# =========================================================

def serialize_benefit(benefit: PlanBenefit):

    return serialize_model(
        benefit,
        BENEFIT_FIELDS
    )


# =========================================================
# CORE FETCH FUNCTIONS
# =========================================================

def get_benefit_by_id(
    db: Session,
    benefit_id: str
):

    benefit = (
        db.query(PlanBenefit)
        .filter(
            PlanBenefit.benefit_id == benefit_id
        )
        .first()
    )

    return serialize_benefit(
        benefit
    )


def get_plan_benefits(
    db: Session,
    plan_id: str
):

    benefits = (
        db.query(PlanBenefit)
        .filter(
            PlanBenefit.plan_id == plan_id
        )
        .all()
    )

    return [
        serialize_benefit(
            benefit
        )
        for benefit in benefits
    ]


def get_benefits_by_type(
    db: Session,
    plan_id: str,
    benefit_type: str
):

    benefits = (
        db.query(PlanBenefit)
        .filter(
            PlanBenefit.plan_id == plan_id,
            PlanBenefit.benefit_type == benefit_type
        )
        .all()
    )

    return [
        serialize_benefit(
            benefit
        )
        for benefit in benefits
    ]


# =========================================================
# COVERAGE FUNCTIONS
# =========================================================

def check_benefit_coverage(
    db: Session,
    plan_id: str,
    benefit_type: str
):

    benefit = (
        db.query(PlanBenefit)
        .filter(
            PlanBenefit.plan_id == plan_id,
            PlanBenefit.benefit_type == benefit_type
        )
        .first()
    )

    if not benefit:
        return False

    return benefit.is_covered


def get_coverage_limit(
    db: Session,
    plan_id: str,
    benefit_type: str
):

    benefit = (
        db.query(PlanBenefit)
        .filter(
            PlanBenefit.plan_id == plan_id,
            PlanBenefit.benefit_type == benefit_type
        )
        .first()
    )

    if not benefit:
        return None

    return (
        float(benefit.coverage_limit)
        if benefit.coverage_limit is not None
        else None
    )