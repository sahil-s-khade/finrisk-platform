import joblib
import pandas as pd

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.model_selection import (
    train_test_split
)

from config.logger import logger


def load_datasets():
    """
    Load ML feature datasets.
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


def split_dataset(X, y):
    """
    Create train/test split.
    """

    logger.info(
        "Creating train/test split..."
    )

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


def train_model(X_train, y_train):
    """
    Train fraud detection model.
    """

    logger.info(
        "Training Random Forest model..."
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

    return model


def evaluate_model(
    model,
    X_test,
    y_test
):
    """
    Evaluate fraud detection model.
    """

    logger.info(
        "Evaluating model..."
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nModel Accuracy:\n")

    print(
        round(accuracy * 100, 2),
        "%"
    )

    print(
        "\nClassification Report:\n"
    )

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    print(
        "\nConfusion Matrix:\n"
    )

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )


def save_model(model):
    """
    Save trained ML model.
    """

    output_path = (
        "models/fraud_detection_model.pkl"
    )

    joblib.dump(
        model,
        output_path
    )

    logger.info(
        f"Model saved to:"
        f" {output_path}"
    )


if __name__ == "__main__":

    logger.info(
        "\nStarting fraud model training...\n"
    )

    X, y = load_datasets()

    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = split_dataset(X, y)

    model = train_model(
        X_train,
        y_train
    )

    evaluate_model(
        model,
        X_test,
        y_test
    )

    save_model(model)

    logger.info(
        "\nFraud model training completed!"
    )