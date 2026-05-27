from sqlalchemy import Column,String, Date, Numeric
from models.base import Base


class Claim(Base):
    __tablename__='claims'
    claim_id = Column(String, primary_key=True)
    policy_id = Column(String)
    member_id = Column(String)
    claim_date = Column(Date)

    claim_amount = Column(Numeric)
    approved_amount = Column(Numeric)

    status = Column(String)
    hospital_name = Column(String)
    claim_type = Column(String)