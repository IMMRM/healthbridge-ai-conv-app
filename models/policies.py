from sqlalchemy import Column, String, Date, Numeric, DateTime
from models.base import Base


class Policy(Base):

    __tablename__ = "policies"

    policy_id = Column(String, primary_key=True)

    plan_id = Column(String, nullable=False)

    policy_holder_id = Column(String, nullable=False)

    sum_assured = Column(Numeric, nullable=False)

    premium_amount = Column(Numeric, nullable=False)

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    status = Column(String, nullable=False)

    remaining_sum = Column(Numeric, nullable=False)

    created_at = Column(DateTime)