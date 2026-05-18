import pandas as pd

from config.logger import logger


VALID_MERCHANT_CATEGORIES = [
    "grocery",
    "electronics",
    "travel",
    "restaurant",
    "fashion",
    "crypto",
    "gaming",
    "healthcare"
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


def check_missing_values(df):
    """
    Detect missing values.
    """

    logger.info(
        "Checking missing values..."
    )

    missing_counts = (
        df.isnull().sum()
    )

    print("\nMissing Values:\n")

    print(
        missing_counts[
            missing_counts > 0
        ]
    )


def check_duplicate_transactions(df):
    """
    Detect duplicate transaction IDs.
    """

    logger.info(
        "Checking duplicate transactions..."
    )

    duplicates = (
        df["transaction_id"]
        .duplicated()
        .sum()
    )

    print(
        f"\nDuplicate Transactions:"
        f" {duplicates}"
    )


def check_negative_amounts(df):
    """
    Detect invalid transaction amounts.
    """

    logger.info(
        "Checking negative amounts..."
    )

    invalid_amounts = df[
        df["amount"] <= 0
    ]

    print(
        f"\nInvalid Amount Records:"
        f" {len(invalid_amounts)}"
    )


def check_invalid_categories(df):
    """
    Detect invalid merchant categories.
    """

    logger.info(
        "Checking merchant categories..."
    )

    invalid_categories = df[
        ~df["merchant_category"]
        .isin(
            VALID_MERCHANT_CATEGORIES
        )
    ]

    print(
        f"\nInvalid Merchant Categories:"
        f" {len(invalid_categories)}"
    )


def check_invalid_user_ids(df):
    """
    Validate user ID format.
    """

    logger.info(
        "Checking user IDs..."
    )

    invalid_users = df[
        ~df["user_id"]
        .astype(str)
        .str.startswith("USER")
    ]

    print(
        f"\nInvalid User IDs:"
        f" {len(invalid_users)}"
    )


def generate_quality_summary(df):
    """
    Generate data quality summary.
    """

    logger.info(
        "Generating quality summary..."
    )

    print("\nData Quality Summary\n")

    print(
        f"Total Records: {len(df)}"
    )

    print(
        f"Fraud Records:"
        f" {df['is_fraud'].sum()}"
    )

    print(
        f"Unique Users:"
        f" {df['user_id'].nunique()}"
    )

    print(
        f"Unique Merchants:"
        f" {df['merchant_category'].nunique()}"
    )


if __name__ == "__main__":

    logger.info(
        "\nStarting data quality checks...\n"
    )

    dataset = load_dataset()

    check_missing_values(dataset)

    check_duplicate_transactions(dataset)

    check_negative_amounts(dataset)

    check_invalid_categories(dataset)

    check_invalid_user_ids(dataset)

    generate_quality_summary(dataset)

    logger.info(
        "\nData quality validation completed!"
    )