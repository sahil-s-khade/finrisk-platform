import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/transactions.csv"
)

print("\nDataset Shape:\n")
print(df.shape)

print("\nColumns:\n")
print(df.columns)

print("\nFraud Distribution:\n")
print(df["is_fraud"].value_counts())

print("\nTransaction Statistics:\n")
print(df["amount"].describe())