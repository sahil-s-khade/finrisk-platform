import pandas as pd

# Load behavioral dataset
df = pd.read_csv(
    "data/behavioral_transactions.csv"
)

print("\nBehavioral Feature Analysis\n")

print(
    "\nRapid Transaction Counts:\n"
)

print(
    df["rapid_transaction_flag"]
    .value_counts()
)

print(
    "\nAverage Time Between Transactions:\n"
)

print(
    df[
        "minutes_since_last_transaction"
    ].describe()
)

print(
    "\nTop Users by Transaction Volume:\n"
)

print(
    df.groupby("user_id")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(
    "\nFraud vs Rapid Transactions:\n"
)

print(
    pd.crosstab(
        df["is_fraud"],
        df["rapid_transaction_flag"]
    )
)