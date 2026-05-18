import pandas as pd

from sklearn.preprocessing import LabelEncoder

from config.logger import logger


def load_dataset():
    """
    Load scored transaction dataset.
    """

    logger.info(
        "Loading scored transaction dataset..."
    )

    df = pd.read_csv(
        "data/scored_transactions.csv"
    )

    return df


def encode_categorical_features(df):
    """
    Encode categorical variables.
    """

    logger.info(
        "Encoding categorical features..."
    )

    categorical_columns = [
        "merchant_category",
        "location",
        "day_of_week",
        "amount_category",
        "risk_level"
    ]

    encoders = {}

    for column in categorical_columns:

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(
            df[column].astype(str)
        )

        encoders[column] = encoder

    return df, encoders


def prepare_feature_matrix(df):
    """
    Create ML feature matrix and labels.
    """

    logger.info(
        "Preparing feature matrix..."
    )

    feature_columns = [

        "amount",

        "transaction_hour",

        "is_high_risk_merchant",

        "amount_log",

        "merchant_category",

        "location",

        "day_of_week",

        "risk_score",

        "rapid_transaction_flag",

        "user_transaction_count",

        "minutes_since_last_transaction",

        "amount_category",

        "risk_level"
    ]

    X = df[feature_columns]

    y = df["is_fraud"]

    return X, y


def save_ml_dataset(X, y):
    """
    Save ML-ready datasets.
    """

    X.to_csv(
        "data/ml_features.csv",
        index=False
    )

    y.to_csv(
        "data/ml_labels.csv",
        index=False
    )

    logger.info(
        "ML datasets saved successfully!"
    )


if __name__ == "__main__":

    logger.info(
        "\nStarting ML dataset preparation...\n"
    )

    dataset = load_dataset()

    dataset, encoders = (
        encode_categorical_features(
            dataset
        )
    )

    X, y = prepare_feature_matrix(
        dataset
    )

    save_ml_dataset(X, y)

    print("\nFeature Matrix Shape:\n")

    print(X.shape)

    print("\nFeature Columns:\n")

    print(X.columns)

    print("\nFraud Distribution:\n")

    print(y.value_counts())

    logger.info(
        "\nML dataset preparation completed!"
    )