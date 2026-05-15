import joblib
import pandas as pd

from sklearn.ensemble import (
    IsolationForest
)

from config.logger import logger


def load_dataset():
    """
    Load ML feature dataset.
    """

    logger.info(
        "Loading ML feature dataset..."
    )

    X = pd.read_csv(
        "data/ml_features.csv"
    )

    return X


def train_anomaly_model(X):
    """
    Train Isolation Forest model.
    """

    logger.info(
        "Training anomaly detection model..."
    )

    model = IsolationForest(

        n_estimators=100,

        contamination=0.05,

        random_state=42
    )

    model.fit(X)

    return model


def save_model(model):
    """
    Save anomaly detection model.
    """

    output_path = (
        "models/anomaly_detection_model.pkl"
    )

    joblib.dump(
        model,
        output_path
    )

    logger.info(
        f"Anomaly model saved to:"
        f" {output_path}"
    )


if __name__ == "__main__":

    logger.info(
        "\nStarting anomaly model training...\n"
    )

    dataset = load_dataset()

    model = train_anomaly_model(
        dataset
    )

    save_model(model)

    logger.info(
        "\nAnomaly model training completed!"
    )