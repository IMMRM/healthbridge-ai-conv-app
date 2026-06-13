from sqlalchemy.orm import Session

from models.members import Member

from utils.serializer import serialize_model


# =========================================================
# SERIALIZATION FIELDS
# =========================================================

MEMBER_FIELDS = [
    "member_id",
    "policy_id",
    "first_name",
    "last_name",
    "gender",
    "dob",
    "email",
    "phone",
    "relationship",
    "coverage_limit"
]


# =========================================================
# SERIALIZER
# =========================================================

def serialize_member(member: Member):

    return serialize_model(
        member,
        MEMBER_FIELDS
    )


# =========================================================
# CORE FETCH FUNCTIONS
# =========================================================

def get_member_by_id(
    db: Session,
    member_id: str
):

    member = (
        db.query(Member)
        .filter(
            Member.member_id == member_id
        )
        .first()
    )

    return serialize_member(
        member
    )


def get_members_by_policy_id(
    db: Session,
    policy_id: str
):

    members = (
        db.query(Member)
        .filter(
            Member.policy_id == policy_id
        )
        .all()
    )

    return [
        serialize_member(member)
        for member in members
    ]


def get_primary_member(
    db: Session,
    policy_id: str
):

    member = (
        db.query(Member)
        .filter(
            Member.policy_id == policy_id,
            Member.relationship == "Self"
        )
        .first()
    )

    return serialize_member(
        member
    )


# =========================================================
# LOOKUP FUNCTIONS
# =========================================================

def get_member_email(
    db: Session,
    member_id: str
):

    member = (
        db.query(Member)
        .filter(
            Member.member_id == member_id
        )
        .first()
    )

    if not member:
        return None

    return member.email


def get_member_phone(
    db: Session,
    member_id: str
):

    member = (
        db.query(Member)
        .filter(
            Member.member_id == member_id
        )
        .first()
    )

    if not member:
        return None

    return member.phone