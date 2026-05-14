import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed_transactions.csv"
)

print("\nDataset Columns:\n")
print(df.columns)

print("\nFraud Distribution:\n")
print(df["is_fraud"].value_counts())

print("\nHigh Risk Merchant Counts:\n")
print(
    df["is_high_risk_merchant"]
    .value_counts()
)

print("\nAmount Category Distribution:\n")
print(
    df["amount_category"]
    .value_counts()
)

print("\nAverage Amount by Fraud Status:\n")
print(
    df.groupby("is_fraud")["amount"]
    .mean()
)