import pandas as pd

from config.database import SessionLocal
from models.transaction import Transaction


BATCH_SIZE = 500


def load_dataset():
    """
    Load processed dataset into PostgreSQL
    using batch inserts.
    """

    print("\nLoading processed dataset...\n")

    # Load processed CSV
    df = pd.read_csv(
        "data/processed_transactions.csv"
    )

    print(
        f"Dataset loaded with shape:"
        f" {df.shape}"
    )

    db = SessionLocal()

    inserted_count = 0

    try:

        transactions_batch = []

        for _, row in df.iterrows():

            # Check duplicate transaction
            existing_transaction = (
                db.query(Transaction)
                .filter(
                    Transaction.transaction_id
                    == row["transaction_id"]
                )
                .first()
            )

            if existing_transaction:
                continue

            transaction = Transaction(
                transaction_id=row["transaction_id"],
                user_id=row["user_id"],
                amount=row["amount"],
                merchant_category=row[
                    "merchant_category"
                ],
                timestamp=row["timestamp"],
                location=row["location"],
                is_fraud=row["is_fraud"],

                # Engineered features
                transaction_hour=row[
                    "transaction_hour"
                ],
                day_of_week=row[
                    "day_of_week"
                ],
                is_high_risk_merchant=row[
                    "is_high_risk_merchant"
                ],
                amount_log=row["amount_log"],
                amount_category=row[
                    "amount_category"
                ]
            )

            transactions_batch.append(
                transaction
            )

            inserted_count += 1

            # Insert batch
            if (
                len(transactions_batch)
                >= BATCH_SIZE
            ):

                db.bulk_save_objects(
                    transactions_batch
                )

                db.commit()

                print(
                    f"Inserted batch:"
                    f" {inserted_count}"
                )

                transactions_batch = []

        # Insert remaining rows
        if transactions_batch:

            db.bulk_save_objects(
                transactions_batch
            )

            db.commit()

        print(
            f"\nSuccessfully inserted"
            f" {inserted_count} transactions!"
        )

    except Exception as e:

        db.rollback()

        print("\nETL load failed!\n")

        print(str(e))

    finally:

        db.close()


if __name__ == "__main__":

    load_dataset()