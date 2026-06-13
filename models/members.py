from sqlalchemy import Column, String, Boolean, Date, Numeric
from models.base import Base


class Member(Base):

    __tablename__ = "members"

    member_id = Column(String, primary_key=True)

    policy_id = Column(String, nullable=False)

    name = Column(String, nullable=False)

    relation = Column(String, nullable=False)

    gender = Column(String, nullable=False)

    coverage_limit = Column(Numeric, nullable=False)

    is_primary = Column(Boolean, nullable=False)

    DOB = Column(Date)

    email = Column(String)

    phone_number = Column(String)