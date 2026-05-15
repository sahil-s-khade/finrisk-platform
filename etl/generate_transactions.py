import random
import uuid
from datetime import datetime, timedelta

import pandas as pd

from config.etl_config import ETLConfig


# Merchant categories
MERCHANT_CATEGORIES = [
    "grocery",
    "electronics",
    "travel",
    "restaurant",
    "fashion",
    "crypto",
    "gaming",
    "healthcare"
]

# Locations
LOCATIONS = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Unknown"
]


def generate_transaction(is_fraud=False):
    """
    Generate a single synthetic transaction.
    """

    # Random transaction timestamp
    timestamp = datetime.now() - timedelta(
        minutes=random.randint(1, 100000)
    )

    # Normal transactions
    amount = round(random.uniform(10, 5000), 2)

    merchant_category = random.choice(
        MERCHANT_CATEGORIES
    )

    location = random.choice(LOCATIONS)

    # Simulate fraud patterns
    if is_fraud:

        amount = round(
            random.uniform(50000, 200000),
            2
        )

        merchant_category = random.choice([
            "crypto",
            "gaming",
            "electronics"
        ])

        location = "Unknown"

    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": f"USER{random.randint(1000, 9999)}",
        "amount": amount,
        "merchant_category": merchant_category,
        "timestamp": timestamp,
        "location": location,
        "is_fraud": is_fraud
    }


def generate_dataset(
    num_transactions=5000,
    fraud_ratio=0.05
):
    """
    Generate synthetic transaction dataset.
    """

    transactions = []

    fraud_count = int(
        num_transactions * fraud_ratio
    )

    normal_count = (
        num_transactions - fraud_count
    )

    print("\nGenerating normal transactions...")

    for _ in range(normal_count):

        transactions.append(
            generate_transaction(
                is_fraud=False
            )
        )

    print("Generating fraudulent transactions...")

    for _ in range(fraud_count):

        transactions.append(
            generate_transaction(
                is_fraud=True
            )
        )

    # Shuffle dataset
    random.shuffle(transactions)

    # Convert to DataFrame
    df = pd.DataFrame(transactions)

    return df


if __name__ == "__main__":

    print(
        "\nStarting synthetic data generation...\n"
    )

    print(
        f"\nConfigured Transactions:"
        f" {ETLConfig.NUM_TRANSACTIONS}"
    )

    print(
        f"Configured Fraud Ratio:"
        f" {ETLConfig.FRAUD_RATIO}"
    )

    dataset = generate_dataset(
        num_transactions=
        ETLConfig.NUM_TRANSACTIONS,

        fraud_ratio=
        ETLConfig.FRAUD_RATIO
    )

    output_path = "data/transactions.csv"

    dataset.to_csv(
        output_path,
        index=False
    )

    print("\nDataset generated successfully!")

    print(f"\nSaved to: {output_path}")

    print("\nDataset Preview:\n")

    print(dataset.head())

    print("\nFraud Distribution:\n")

    print(
        dataset["is_fraud"]
        .value_counts()
    )