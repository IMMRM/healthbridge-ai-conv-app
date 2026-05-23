from sqlalchemy import Column, String
from models.base import Base


class Plan(Base):

    __tablename__ = "plans"

    plan_id = Column(String, primary_key=True)

    plan_name = Column(String, nullable=False)

    insurer_name = Column(String, nullable=False)

    plan_type = Column(String, nullable=False)

    description = Column(String)