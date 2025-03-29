import pandas as pd
from pymongo import MongoClient
from fraud_detection.models.fraud_detection_model import FraudDetectionModel



def create_connection():
    """Create a database connection to the MongoDB database."""
    client = MongoClient('mongodb://localhost:27017/')
    return client['fraud_detection']

def load_data():
    """Load data from MongoDB."""
    db = create_connection()
    transactions_collection = db['transactions']
    data = pd.DataFrame(list(transactions_collection.find()))
    return data

if __name__ == "__main__":
    data = load_data()
    model = FraudDetectionModel()
    model.train(data)
    predictions = model.predict(data)
    print(predictions)
