import joblib
import pandas as pd


# Load anomaly model
model = joblib.load(
    "models/anomaly_detection_model.pkl"
)


def detect_anomaly(features):
    """
    Detect anomalous transactions.
    """

    input_df = pd.DataFrame(
        [features]
    )

    prediction = model.predict(
        input_df
    )[0]

    anomaly_score = (
        model.decision_function(
            input_df
        )[0]
    )

    is_anomaly = (
        prediction == -1
    )

    return {

        "is_anomaly":
            bool(is_anomaly),

        "anomaly_score":
            round(
                float(anomaly_score),
                4
            )
    }