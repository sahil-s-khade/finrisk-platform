import joblib
import pandas as pd

# Load model
model = joblib.load(
    "models/fraud_detection_model.pkl"
)

# Load feature names
X = pd.read_csv(
    "data/ml_features.csv"
)

# Get feature importance
importance = pd.DataFrame({

    "feature": X.columns,

    "importance":
        model.feature_importances_
})

# Sort descending
importance = importance.sort_values(
    by="importance",
    ascending=False
)

print("\nFeature Importance:\n")

print(importance)