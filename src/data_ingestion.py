import pandas as pd

def load_data():
    df = pd.read_csv("data/Customer-Churn .csv")

    print("\n✅ Data Loaded Successfully")
    print("\n🔹 First 5 Rows:\n", df.head())
    print("\n🔹 Shape:", df.shape)
    print("\n🔹 Columns:", df.columns)
    print(df.columns)

    return df