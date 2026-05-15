import uuid

import joblib
import pandas as pd

from config.database import SessionLocal

from models.prediction_log import (
    PredictionLog
)


# Load trained model
from ml.model_registry import (
    get_latest_model
)

LATEST_MODEL = get_latest_model()

model = joblib.load(
    LATEST_MODEL
)


def predict_fraud(features):
    """
    Perform fraud prediction
    and log inference.
    """

    db = SessionLocal()

    try:

        # Convert features to DataFrame
        input_df = pd.DataFrame(
            [features]
        )

        # Fraud prediction
        prediction = model.predict(
            input_df
        )[0]

        # Fraud probability
        probability = (
            model.predict_proba(
                input_df
            )[0][1]
        )

        result = {
            "is_fraud": bool(prediction),
            "fraud_probability": float(
    round(
        probability * 100,
        2
    )
)
        }

        # Create audit log
        prediction_log = PredictionLog(

            transaction_id=str(
                uuid.uuid4()
            ),

            prediction=str(
                result["is_fraud"]
            ),

          fraud_probability=float(
    result[
        "fraud_probability"
    ]
),

            model_version="v1.0"
        )

        db.add(prediction_log)

        db.commit()

        return result

    except Exception as e:

        db.rollback()

        raise e

    finally:

        db.close()