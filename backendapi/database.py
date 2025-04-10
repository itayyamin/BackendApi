"""
Database configuration for SQLAlchemy.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment or use a default SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# Create engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()


def get_db():
    """
    Get database session.
    
    Returns:
        Session: SQLAlchemy session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()