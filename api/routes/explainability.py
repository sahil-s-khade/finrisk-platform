from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required


explainability_bp = Blueprint(
    "explainability",
    __name__
)


@explainability_bp.route(
    "/explain-fraud",
    methods=["POST"]
)
@jwt_required()
def explain_fraud():

    data = request.get_json()

    print("RECEIVED DATA:", data)

    explanations = []


    # Extract values

    amount = data.get("amount", 0)

    risk_score = data.get("risk_score", 0)

    location = data.get("location", 0)

    high_risk_merchant = data.get(
        "is_high_risk_merchant", 0
    )

    rapid_transaction_flag = data.get(
        "rapid_transaction_flag", 0
    )


    # Fraud Rules

    if amount > 100000:

        explanations.append(
            "Unusually high transaction amount"
        )


    if high_risk_merchant == 1:

        explanations.append(
            "High-risk merchant category"
        )


    if rapid_transaction_flag == 1:

        explanations.append(
            "Multiple rapid transactions detected"
        )


    if location == 7:

        explanations.append(
            "Suspicious transaction location"
        )


    if risk_score > 90:

        explanations.append(
            "Very high fraud risk score"
        )


    # Final prediction

    fraud_prediction = len(explanations) >= 2


    response = {

        "fraud_prediction":
            fraud_prediction,

        "risk_score":
            risk_score,

        "explanations":
            explanations
    }

    print("FINAL RESPONSE:", response)

    return jsonify(response), 200