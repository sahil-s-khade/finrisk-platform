from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from flask_jwt_extended import jwt_required

from sqlalchemy import func

from api.schemas.transaction_schema import TransactionSchema

from config.database import SessionLocal
from models.transaction import Transaction

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