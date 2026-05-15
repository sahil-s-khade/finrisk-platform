from services.fraud_detection_service import (
    predict_fraud
)

from services.anomaly_detection_service import (
    detect_anomaly
)


def ensemble_fraud_analysis(features):
    """
    Combine multiple fraud engines.
    """

    # Supervised ML prediction
    ml_result = predict_fraud(
        features
    )

    # Anomaly detection
    anomaly_result = detect_anomaly(
        features
    )

    fraud_probability = (
        ml_result[
            "fraud_probability"
        ]
    )

    is_anomaly = (
        anomaly_result[
            "is_anomaly"
        ]
    )

    # Ensemble decision logic
    if fraud_probability >= 80:

        final_decision = "HIGH_FRAUD_RISK"

    elif (
        fraud_probability >= 50
        or is_anomaly
    ):

        final_decision = (
            "MEDIUM_FRAUD_RISK"
        )

    else:

        final_decision = (
            "LOW_FRAUD_RISK"
        )

    return {

        "ml_prediction":
            ml_result,

        "anomaly_detection":
            anomaly_result,

        "final_decision":
            final_decision
    }