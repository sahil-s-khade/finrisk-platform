from marshmallow import Schema, fields, validate


class TransactionSchema(Schema):
    """
    Validates incoming transaction payloads.
    """

    transaction_id = fields.String(
        required=True
    )

    user_id = fields.String(
        required=True
    )

    amount = fields.Float(
        required=True,
        validate=validate.Range(min=0.01)
    )

    merchant_category = fields.String(
        required=True
    )

    location = fields.String(
        required=True
    )

    is_fraud = fields.Boolean(
        required=False
    )