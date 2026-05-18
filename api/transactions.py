from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from flask_jwt_extended import jwt_required

from sqlalchemy import func

from api.schemas.transaction_schema import TransactionSchema

from config.database import SessionLocal
from models.transaction import Transaction

from services.fraud_detection_service import (
    predict_fraud
)

from models.prediction_log import (
    PredictionLog
)

from models.prediction_log import (
    PredictionLog
)

from services.anomaly_detection_service import (
    detect_anomaly
)

from services.ensemble_fraud_service import (
    ensemble_fraud_analysis
)


from services.explainability_service import (
    explain_prediction
)

from models.prediction_log import (
    PredictionLog
)

# Create Blueprint
transaction_bp = Blueprint(
    "transactions",
    __name__
)

# Initialize schema
transaction_schema = TransactionSchema()


@transaction_bp.route(
    "/transactions",
    methods=["POST"]
)
@jwt_required()
def create_transaction():
    """
    Create and store transaction.
    """

    db = SessionLocal()

    try:
        # Get request JSON
        data = request.get_json()

        # Validate payload
        validated_data = transaction_schema.load(data)

        # Create transaction object
        transaction = Transaction(
            transaction_id=validated_data["transaction_id"],
            user_id=validated_data["user_id"],
            amount=validated_data["amount"],
            merchant_category=validated_data["merchant_category"],
            location=validated_data["location"],
            is_fraud=validated_data.get("is_fraud", False)
        )

        # Save to database
        db.add(transaction)

        # Commit transaction
        db.commit()

        # Refresh object from DB
        db.refresh(transaction)

        return jsonify({
            "message": "Transaction created successfully",
            "transaction": {
                "id": transaction.id,
                "transaction_id": transaction.transaction_id,
                "user_id": transaction.user_id,
                "amount": transaction.amount,
                "merchant_category": transaction.merchant_category,
                "location": transaction.location,
                "is_fraud": transaction.is_fraud
            }
        }), 201

    except ValidationError as err:

        return jsonify({
            "errors": err.messages
        }), 400

    except Exception as e:

        # Rollback failed transaction
        db.rollback()

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()


@transaction_bp.route(
    "/transactions",
    methods=["GET"]
)
@jwt_required()
def get_transactions():
    """
    Retrieve all transactions.
    """

    db = SessionLocal()

    try:

        transactions = db.query(Transaction).all()

        results = []

        for txn in transactions:

            results.append({
                "id": txn.id,
                "transaction_id": txn.transaction_id,
                "user_id": txn.user_id,
                "amount": txn.amount,
                "merchant_category": txn.merchant_category,
                "location": txn.location,
                "is_fraud": txn.is_fraud,
                "risk_score": txn.risk_score
            })

        return jsonify({
            "count": len(results),
            "transactions": results
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()


@transaction_bp.route(
    "/transactions/fraud",
    methods=["GET"]
)
@jwt_required()
def get_fraud_transactions():
    """
    Retrieve fraudulent transactions only.
    """

    db = SessionLocal()

    try:

        fraud_transactions = (
            db.query(Transaction)
            .filter(Transaction.is_fraud == True)
            .all()
        )

        results = []

        for txn in fraud_transactions:

            results.append({
                "transaction_id": txn.transaction_id,
                "user_id": txn.user_id,
                "amount": txn.amount,
                "merchant_category": txn.merchant_category,
                "location": txn.location
            })

        return jsonify({
            "fraud_count": len(results),
            "fraud_transactions": results
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()


@transaction_bp.route(
    "/analytics",
    methods=["GET"]
)
@jwt_required()
def get_analytics():
    """
    Basic transaction analytics.
    """

    db = SessionLocal()

    try:

        total_transactions = (
            db.query(Transaction)
            .count()
        )

        fraud_transactions = (
            db.query(Transaction)
            .filter(Transaction.is_fraud == True)
            .count()
        )

        total_amount = (
            db.query(func.sum(Transaction.amount))
            .scalar()
        )

        avg_amount = (
            db.query(func.avg(Transaction.amount))
            .scalar()
        )

        fraud_rate = 0

        if total_transactions > 0:
            fraud_rate = (
                fraud_transactions / total_transactions
            ) * 100

        return jsonify({
            "total_transactions": total_transactions,
            "fraud_transactions": fraud_transactions,
            "fraud_rate_percent": round(fraud_rate, 2),
            "total_transaction_amount": float(total_amount or 0),
            "average_transaction_amount": round(
                float(avg_amount or 0), 2
            )
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()


@transaction_bp.route(
    "/transactions/high-risk",
    methods=["GET"]
)
@jwt_required()
def get_high_risk_transactions():
    """
    Retrieve high-risk transactions.
    """

    db = SessionLocal()

    try:

        transactions = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "HIGH"
            )
            .all()
        )

        results = []

        for txn in transactions:

            results.append({
                "transaction_id":
                    txn.transaction_id,

                "user_id":
                    txn.user_id,

                "amount":
                    txn.amount,

                "merchant_category":
                    txn.merchant_category,

                "location":
                    txn.location,

                "risk_score":
                    txn.risk_score,

                "risk_level":
                    txn.risk_level
            })

        return jsonify({
            "count": len(results),
            "high_risk_transactions":
                results
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()


@transaction_bp.route(
    "/analytics/risk-summary",
    methods=["GET"]
)
@jwt_required()
def get_risk_summary():
    """
    Risk analytics summary.
    """

    db = SessionLocal()

    try:

        high_risk_count = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "HIGH"
            )
            .count()
        )

        medium_risk_count = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "MEDIUM"
            )
            .count()
        )

        low_risk_count = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "LOW"
            )
            .count()
        )

        avg_risk_score = (
            db.query(
                func.avg(
                    Transaction.risk_score
                )
            ).scalar()
        )

        return jsonify({
            "high_risk_transactions":
                high_risk_count,

            "medium_risk_transactions":
                medium_risk_count,

            "low_risk_transactions":
                low_risk_count,

            "average_risk_score":
                round(
                    float(avg_risk_score or 0),
                    2
                )
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()

@transaction_bp.route(
    "/predict-fraud",
    methods=["POST"]
)
@jwt_required()
def predict_transaction_fraud():
    """
    Real-time fraud prediction API.
    """

    try:

        data = request.get_json()

        prediction = predict_fraud(data)

        return jsonify({
            "prediction": prediction
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

@transaction_bp.route(
    "/analytics/prediction-logs",
    methods=["GET"]
)
@jwt_required()
def get_prediction_logs():
    """
    Retrieve ML prediction logs.
    """

    db = SessionLocal()

    try:

        logs = (
            db.query(PredictionLog)
            .order_by(
                PredictionLog.created_at
                .desc()
            )
            .limit(50)
            .all()
        )

        results = []

        for log in logs:

            results.append({

                "transaction_id":
                    log.transaction_id,

                "prediction":
                    log.prediction,

                "fraud_probability":
                    log.fraud_probability,

                "model_version":
                    log.model_version,

                "created_at":
                    log.created_at
            })

        return jsonify({
            "prediction_logs":
                results
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()

@transaction_bp.route(
    "/analytics/model-monitoring",
    methods=["GET"]
)
@jwt_required()
def model_monitoring_dashboard():
    """
    ML monitoring dashboard API.
    """

    db = SessionLocal()

    try:

        total_predictions = (
            db.query(
                PredictionLog
            ).count()
        )

        fraud_predictions = (
            db.query(
                PredictionLog
            )
            .filter(
                PredictionLog.prediction
                == "True"
            )
            .count()
        )

        avg_probability = (
            db.query(
                func.avg(
                    PredictionLog
                    .fraud_probability
                )
            ).scalar()
        )

        return jsonify({

            "total_predictions":
                total_predictions,

            "fraud_predictions":
                fraud_predictions,

            "average_fraud_probability":
                round(
                    float(
                        avg_probability or 0
                    ),
                    2
                )
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()

@transaction_bp.route(
    "/detect-anomaly",
    methods=["POST"]
)
@jwt_required()
def detect_transaction_anomaly():
    """
    Unsupervised anomaly detection API.
    """

    try:

        data = request.get_json()

        result = detect_anomaly(
            data
        )

        return jsonify({
            "anomaly_detection":
                result
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
    
@transaction_bp.route(
    "/ensemble-fraud-analysis",
    methods=["POST"]
)
@jwt_required()
def ensemble_fraud_detection():
    """
    Hybrid fraud intelligence API.
    """

    try:

        data = request.get_json()

        result = (
            ensemble_fraud_analysis(
                data
            )
        )

        return jsonify({
            "ensemble_analysis":
                result
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@transaction_bp.route(
    "/explain-fraud",
    methods=["POST"]
)
@jwt_required()
def explain_fraud_prediction():
    """
    Explain fraud prediction.
    """

    try:

        data = request.get_json()

        explanation = explain_prediction(
            data
        )

        return jsonify({
            "explanation":
                explanation
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
    
@transaction_bp.route(
    "/dashboard/overview",
    methods=["GET"]
)
@jwt_required()
def fraud_dashboard_overview():
    """
    Unified fraud intelligence dashboard.
    """

    db = SessionLocal()

    try:

        # Transaction metrics
        total_transactions = (
            db.query(Transaction)
            .count()
        )

        fraud_transactions = (
            db.query(Transaction)
            .filter(
                Transaction.is_fraud
                == True
            )
            .count()
        )

        high_risk_transactions = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "HIGH"
            )
            .count()
        )

        avg_transaction_amount = (
            db.query(
                func.avg(
                    Transaction.amount
                )
            ).scalar()
        )

        # Prediction metrics
        total_predictions = (
            db.query(
                PredictionLog
            ).count()
        )

        fraud_predictions = (
            db.query(
                PredictionLog
            )
            .filter(
                PredictionLog.prediction
                == "True"
            )
            .count()
        )

        avg_fraud_probability = (
            db.query(
                func.avg(
                    PredictionLog
                    .fraud_probability
                )
            ).scalar()
        )

        # Risk distribution
        low_risk = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "LOW"
            )
            .count()
        )

        medium_risk = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "MEDIUM"
            )
            .count()
        )

        high_risk = (
            db.query(Transaction)
            .filter(
                Transaction.risk_level
                == "HIGH"
            )
            .count()
        )

        return jsonify({

            "transaction_metrics": {

                "total_transactions":
                    total_transactions,

                "fraud_transactions":
                    fraud_transactions,

                "high_risk_transactions":
                    high_risk_transactions,

                "average_transaction_amount":
                    round(
                        float(
                            avg_transaction_amount
                            or 0
                        ),
                        2
                    )
            },

            "ml_prediction_metrics": {

                "total_predictions":
                    total_predictions,

                "fraud_predictions":
                    fraud_predictions,

                "average_fraud_probability":
                    round(
                        float(
                            avg_fraud_probability
                            or 0
                        ),
                        2
                    )
            },

            "risk_distribution": {

                "low_risk":
                    low_risk,

                "medium_risk":
                    medium_risk,

                "high_risk":
                    high_risk
            }

        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()


from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

transactions_bp = Blueprint("transactions", __name__)


@transactions_bp.route("/recent", methods=["GET"])
@jwt_required()
def get_recent_transactions():

    sample_transactions = [

        {
            "transaction_id": "TXN-1001",
            "amount": 1200,
            "risk_score": 12,
            "status": "SAFE"
        },

        {
            "transaction_id": "TXN-1002",
            "amount": 98000,
            "risk_score": 91,
            "status": "FRAUD"
        },

        {
            "transaction_id": "TXN-1003",
            "amount": 4500,
            "risk_score": 32,
            "status": "SAFE"
        }

    ]

    return jsonify(sample_transactions), 200