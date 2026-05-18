from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config.settings import Config

# Create SQLAlchemy engine
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True  # Logs SQL queries (great for development)
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all database models
Base = declarative_base()


def get_db():
    """
    Creates and manages database sessions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()