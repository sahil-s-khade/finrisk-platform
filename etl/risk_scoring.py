import pandas as pd

from config.logger import logger


HIGH_RISK_MERCHANTS = [
    "crypto",
    "gaming",
    "electronics"
]


def load_dataset():
    """
    Load behavioral transaction dataset.
    """

    logger.info(
        "Loading behavioral dataset..."
    )

    df = pd.read_csv(
        "data/behavioral_transactions.csv"
    )

    return df


def calculate_risk_score(row):
    """
    Calculate fraud risk score.
    """

    score = 0

    # High transaction amount
    if row["amount"] > 100000:
        score += 40

    # High-risk merchant
    if (
        row["merchant_category"]
        in HIGH_RISK_MERCHANTS
    ):
        score += 25

    # Unknown location
    if row["location"] == "Unknown":
        score += 20

    # Rapid transactions
    if row["rapid_transaction_flag"] == 1:
        score += 15

    return min(score, 100)


def classify_risk(score):
    """
    Classify fraud severity.
    """

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    return "LOW"


def apply_risk_scoring(df):
    """
    Apply fraud scoring engine.
    """

    logger.info(
        "Applying fraud risk scoring..."
    )

    df["risk_score"] = (
        df.apply(
            calculate_risk_score,
            axis=1
        )
    )

    df["risk_level"] = (
        df["risk_score"]
        .apply(classify_risk)
    )

    return df


def save_scored_dataset(df):
    """
    Save scored dataset.
    """

    output_path = (
        "data/scored_transactions.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    logger.info(
        f"Scored dataset saved to:"
        f" {output_path}"
    )


if __name__ == "__main__":

    logger.info(
        "\nStarting fraud risk scoring...\n"
    )

    dataset = load_dataset()

    dataset = apply_risk_scoring(
        dataset
    )

    save_scored_dataset(dataset)

    print("\nRisk Score Distribution:\n")

    print(
        dataset["risk_level"]
        .value_counts()
    )

    print("\nTop High-Risk Transactions:\n")

    print(
        dataset[
            dataset["risk_level"]
            == "HIGH"
        ][[
            "transaction_id",
            "amount",
            "merchant_category",
            "location",
            "risk_score"
        ]].head()
    )

    logger.info(
        "\nFraud scoring completed!"
    )