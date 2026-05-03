from sqlalchemy import Column, String
from app.db.database import Base

from sqlalchemy import Column, String, Boolean, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = "members"

    member_id = Column(String, primary_key=True)
    policy_id = Column(String)  # Foreign key reference
    name = Column(String)
    relation = Column(String)
    gender = Column(String)
    coverage_limit = Column(Numeric)
    is_primary = Column(Boolean)
    DOB = Column(Date)
    email = Column(String)
    phone_number = Column(String)