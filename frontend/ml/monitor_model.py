import pandas as pd

from config.database import SessionLocal

from models.prediction_log import (
    PredictionLog
)


def load_prediction_logs():
    """
    Load prediction audit logs.
    """

    db = SessionLocal()

    try:

        logs = db.query(
            PredictionLog
        ).all()

        records = []

        for log in logs:

            records.append({

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

        return pd.DataFrame(records)

    finally:

        db.close()


def analyze_prediction_distribution(df):
    """
    Analyze fraud predictions.
    """

    print(
        "\nPrediction Distribution:\n"
    )

    print(
        df["prediction"]
        .value_counts()
    )


def analyze_probability_statistics(df):
    """
    Analyze fraud probabilities.
    """

    print(
        "\nFraud Probability Statistics:\n"
    )

    print(
        df["fraud_probability"]
        .describe()
    )


def analyze_model_versions(df):
    """
    Analyze model version usage.
    """

    print(
        "\nModel Version Usage:\n"
    )

    print(
        df["model_version"]
        .value_counts()
    )


def detect_probability_drift(df):
    """
    Simple drift detection logic.
    """

    avg_probability = (
        df["fraud_probability"]
        .mean()
    )

    print(
        "\nAverage Fraud Probability:\n"
    )

    print(
        round(avg_probability, 2)
    )

    if avg_probability > 80:

        print(
            "\nWARNING:"
            " Potential fraud spike detected!"
        )

    elif avg_probability < 5:

        print(
            "\nWARNING:"
            " Potential model under-detection!"
        )


if __name__ == "__main__":

    print(
        "\nStarting model monitoring...\n"
    )

    logs_df = load_prediction_logs()

    if logs_df.empty:

        print(
            "\nNo prediction logs found."
        )

    else:

        analyze_prediction_distribution(
            logs_df
        )

        analyze_probability_statistics(
            logs_df
        )

        analyze_model_versions(
            logs_df
        )

        detect_probability_drift(
            logs_df
        )

    print(
        "\nModel monitoring completed!"
    )