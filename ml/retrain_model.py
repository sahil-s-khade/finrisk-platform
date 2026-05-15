from datetime import datetime

import joblib
import pandas as pd

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score
)

from sklearn.model_selection import (
    train_test_split
)

from config.logger import logger


def load_datasets():
    """
    Load ML datasets.
    """

    logger.info(
        "Loading ML datasets..."
    )

    X = pd.read_csv(
        "data/ml_features.csv"
    )

    y = pd.read_csv(
        "data/ml_labels.csv"
    )

    return X, y


def retrain_model():
    """
    Retrain fraud detection model.
    """

    logger.info(
        "\nStarting model retraining...\n"
    )

    X, y = load_datasets()

    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )

    model.fit(
        X_train,
        y_train.values.ravel()
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nRetrained Model Accuracy:\n")

    print(
        round(accuracy * 100, 2),
        "%"
    )

    # Create version timestamp
    version = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    model_path = (
        f"models/trained_models/"
        f"fraud_model_{version}.pkl"
    )

    # Save versioned model
    joblib.dump(
        model,
        model_path
    )

    print(
        f"\nModel saved to:\n"
        f"{model_path}"
    )

    logger.info(
        "\nModel retraining completed!"
    )


if __name__ == "__main__":

    retrain_model()