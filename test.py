# test_db.py

from sqlalchemy import text
from tools.db import SessionLocal

db = SessionLocal()

print("Session created")

db.execute(text("SELECT * from claims"))

print("Connection successful")