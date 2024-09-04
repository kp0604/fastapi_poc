from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAL_DB_URL =  "postgresql://postgres:postgres@5433/fastapi"

engine  =  create_engine(SQLAL_DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()