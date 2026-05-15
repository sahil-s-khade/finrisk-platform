import joblib
import pandas as pd


# Load trained model
model = joblib.load(
    "models/fraud_detection_model.pkl"
)


FEATURE_NAMES = [

    "amount",

    "transaction_hour",

    "is_high_risk_merchant",

    "amount_log",

    "merchant_category",

    "location",

    "day_of_week",

    "risk_score",

    "rapid_transaction_flag",

    "user_transaction_count",

    "minutes_since_last_transaction",

    "amount_category",

    "risk_level"
]


def explain_prediction(features):
    """
    Generate fraud explanation.
    """

    input_df = pd.DataFrame(
        [features]
    )

    # Feature importance
    importances = (
        model.feature_importances_
    )

    feature_scores = []

    for feature, importance in zip(
        FEATURE_NAMES,
        importances
    ):

        feature_scores.append({

            "feature": feature,

            "importance": round(
                float(importance),
                4
            ),

            "input_value":
                features.get(feature)
        })

    # Sort descending
    feature_scores = sorted(

        feature_scores,

        key=lambda x:
            x["importance"],

        reverse=True
    )

    # Top explanations
    top_features = (
        feature_scores[:5]
    )

    return {

        "top_risk_factors":
            top_features
    }