from sqlalchemy import Column, String, Numeric
from .base import Base


class ClaimsBreakup(Base):
    __tablename__ = 'claim_breakup'

    breakup_id = Column(String, primary_key=True)

    claim_id = Column(String, nullable=False)

    benefit_type = Column(String, nullable=False)

    sub_type = Column(String, nullable=False)

    amount = Column(Numeric, nullable=False)

    approved_amount = Column(Numeric, nullable=False)

    remarks = Column(String)