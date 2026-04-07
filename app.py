from src.data_ingestion import load_data
from src.preprocessing import clean_data
from src.model_training import train_model

def run_pipeline():
    print("Pipeline Started...")

    data = load_data()
    X, y = clean_data(data)
    model = train_model(X, y)

    print("Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()