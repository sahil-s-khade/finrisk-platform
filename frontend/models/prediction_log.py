from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from config.database import Base


class PredictionLog(Base):
    """
    ML prediction audit log.
    """

    __tablename__ = "prediction_logs"

    id = Column(
        Integer,
        primary_key=True
    )

    transaction_id = Column(
        String,
        nullable=False
    )

    prediction = Column(
        String,
        nullable=False
    )

    fraud_probability = Column(
        Float,
        nullable=False
    )

    model_version = Column(
        String,
        default="v1.0"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )