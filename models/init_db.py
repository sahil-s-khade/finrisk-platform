from config.database import engine, Base

# Import all models here
from models.transaction import Transaction

from models.prediction_log import (
    PredictionLog
)


def initialize_database():
    """
    Creates all database tables.
    """

    print("\nCreating database tables...\n")

    Base.metadata.create_all(bind=engine)

    print(" Database tables created successfully!")


if __name__ == "__main__":
    initialize_database()