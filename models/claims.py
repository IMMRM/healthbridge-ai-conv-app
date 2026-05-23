from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

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