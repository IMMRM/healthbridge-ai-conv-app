from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.member import MemberQueryParams
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models.member import Member

router = APIRouter()

@router.get("/member")
def get_member(
    params: MemberQueryParams = Depends(),
    db: Session = Depends(get_db)
):
    email = params.email
    phone = params.phone
    memberId = params.memberId
    if not any([email, phone, memberId]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide at least one of: email, phone, memberId"
        )

    member = None

    if params.email:
        member = db.query(Member).filter(Member.email == params.email).first()

    elif params.phone:
        member = db.query(Member).filter(Member.phone_number == params.phone).first()

    elif params.memberId:
        member = db.query(Member).filter(Member.member_id == params.memberId).first()

    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    return member