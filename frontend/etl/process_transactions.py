import numpy as np
import pandas as pd


# High-risk merchant categories
HIGH_RISK_MERCHANTS = [
    "crypto",
    "gaming",
    "electronics"
]


def clean_dataset(df):
    """
    Clean transaction dataset.
    """

    print("\nCleaning dataset...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert timestamp column
    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    return df


def engineer_features(df):
    """
    Create fraud detection features.
    """

    print("Engineering features...")

    # Transaction hour
    df["transaction_hour"] = (
        df["timestamp"].dt.hour
    )

    # Day of week
    df["day_of_week"] = (
        df["timestamp"].dt.day_name()
    )

    # High-risk merchant flag
    df["is_high_risk_merchant"] = (
        df["merchant_category"]
        .isin(HIGH_RISK_MERCHANTS)
        .astype(int)
    )

    # Log-transform amount
    df["amount_log"] = np.log1p(
        df["amount"]
    )

    # Transaction amount category
    df["amount_category"] = pd.cut(
        df["amount"],
        bins=[0, 1000, 10000, 50000, 500000],
        labels=[
            "low",
            "medium",
            "high",
            "very_high"
        ]
    )

    return df


def save_processed_dataset(df):
    """
    Save processed dataset.
    """

    output_path = (
        "data/processed_transactions.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nProcessed dataset saved to:"
        f" {output_path}"
    )


if __name__ == "__main__":

    print(
        "\nStarting ETL processing pipeline...\n"
    )

    # Load raw dataset
    dataset = pd.read_csv(
        "data/transactions.csv"
    )

    print(
        f"Loaded dataset shape:"
        f" {dataset.shape}"
    )

    # Clean dataset
    dataset = clean_dataset(dataset)

    # Feature engineering
    dataset = engineer_features(dataset)

    # Save processed dataset
    save_processed_dataset(dataset)

    print("\nETL processing complete!")

    print("\nProcessed Dataset Preview:\n")

    print(dataset.head())