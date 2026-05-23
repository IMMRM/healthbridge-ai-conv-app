from sqlalchemy import Column, String
from models.base import Base


class PlanBenefit(Base):

    __tablename__ = "plan_benefits"

    benefit_id = Column(String, primary_key=True)

    plan_id = Column(String, nullable=False)

    benefit_type = Column(String, nullable=False)

    sub_type = Column(String, nullable=False)

    coverage_limit = Column(String, nullable=False)

    coverage_unit = Column(String)

    waiting_period = Column(String)

    limit_type = Column(String)

    remarks = Column(String)