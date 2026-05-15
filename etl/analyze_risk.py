import pandas as pd

# Load scored dataset
df = pd.read_csv(
    "data/scored_transactions.csv"
)

print("\nRisk Level Distribution:\n")

print(
    df["risk_level"]
    .value_counts()
)

print(
    "\nAverage Risk Score by Fraud Status:\n"
)

print(
    df.groupby("is_fraud")[
        "risk_score"
    ].mean()
)

print(
    "\nHigh Risk Fraud Transactions:\n"
)

high_risk_fraud = df[
    (df["risk_level"] == "HIGH")
    &
    (df["is_fraud"] == True)
]

print(
    high_risk_fraud[
        [
            "transaction_id",
            "amount",
            "merchant_category",
            "risk_score"
        ]
    ].head(10)
)