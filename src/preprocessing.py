import pandas as pd

def clean_data(df):
    print("Starting Data Cleaning...")

    # Remove spaces
    df.columns = df.columns.str.strip()

    # Convert target FIRST
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Drop missing values
    df = df.dropna()

    # Separate target
    y = df["Churn"]
    X = df.drop("Churn", axis=1)

    # Convert categorical features
    X = pd.get_dummies(X)

    print("Data Cleaning Completed")

    return X, y