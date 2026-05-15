import pandas as pd


def load_dataset():
    """
    Load processed transaction dataset.
    """

    print("\nLoading processed dataset...\n")

    df = pd.read_csv(
        "data/processed_transactions.csv"
    )

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    return df


def create_behavioral_features(df):
    """
    Engineer behavioral fraud features.
    """

    print("Creating behavioral features...\n")

    # Sort by user and timestamp
    df = df.sort_values(
        by=["user_id", "timestamp"]
    )

    # Transaction count per user
    df["user_transaction_count"] = (
        df.groupby("user_id")
        .cumcount() + 1
    )

    # Cumulative user spending
    df["user_cumulative_amount"] = (
        df.groupby("user_id")["amount"]
        .cumsum()
    )

    # Previous transaction timestamp
    df["previous_transaction_time"] = (
        df.groupby("user_id")["timestamp"]
        .shift(1)
    )

    # Time difference between transactions
    df["minutes_since_last_transaction"] = (
        (
            df["timestamp"]
            - df["previous_transaction_time"]
        )
        .dt.total_seconds() / 60
    )

    # Fill first transaction NaN values
    df[
        "minutes_since_last_transaction"
    ] = df[
        "minutes_since_last_transaction"
    ].fillna(999999)

    # Rapid transaction flag
    df["rapid_transaction_flag"] = (
        df["minutes_since_last_transaction"]
        < 5
    ).astype(int)

    return df


def save_behavioral_dataset(df):
    """
    Save enhanced dataset.
    """

    output_path = (
        "data/behavioral_transactions.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"\nBehavioral dataset saved to:"
        f" {output_path}"
    )


if __name__ == "__main__":

    print(
        "\nStarting behavioral feature pipeline...\n"
    )

    dataset = load_dataset()

    dataset = create_behavioral_features(
        dataset
    )

    save_behavioral_dataset(dataset)

    print("\nBehavioral features created!")

    print("\nDataset Preview:\n")

    print(dataset.head())