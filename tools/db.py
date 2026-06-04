import os

from urllib.parse import quote_plus

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()


# =====================================================
# READ ENV VARIABLES
# =====================================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_USER = os.getenv("DB_USER")

# IMPORTANT
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

DB_NAME = os.getenv("DB_NAME")


# =====================================================
# DATABASE URL
# =====================================================

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


print("DATABASE_URL =", DATABASE_URL)


# =====================================================
# SQLALCHEMY ENGINE
# =====================================================

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)