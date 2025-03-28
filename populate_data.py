import pandas as pd
from pymongo import MongoClient

def create_connection():
    """Create a database connection to the MongoDB database."""
    client = MongoClient('mongodb://localhost:27017/')
    return client['fraud_detection']

def populate_data_from_csv(file_paths):

    """Populate the database with data from a CSV file."""
    db = create_connection()
    transactions_collection = db['transactions']
    
    # Read the CSV file
    for file_path in file_paths:
        data = pd.read_csv(file_path)

    
    # Insert each record into the MongoDB collection
        for index, row in data.iterrows():
            transactions_collection.insert_one({
                'timestamp': row.get('timestamp', None),
                'amount': row.get('amount', None),
                'transaction_type': row.get('transaction_type', None),
                'anomaly': row.get('anomaly', None)
            })


if __name__ == '__main__':
    populate_data_from_csv([
        'fraud_detection/data/Customer Profiles/account_activity.csv',
        'fraud_detection/data/Customer Profiles/customer_data.csv',
        'fraud_detection/data/Fraudulent Patterns/fraud_indicators.csv',
        'fraud_detection/data/Fraudulent Patterns/suspicious_activity.csv',
        'fraud_detection/data/Merchant Information/merchant_data.csv',
        'fraud_detection/data/Merchant Information/transaction_category_labels.csv',
        'fraud_detection/data/Transaction Amounts/amount_data.csv',
        'fraud_detection/data/Transaction Amounts/anomaly_scores.csv',
        'fraud_detection/data/Transaction Data/transaction_metadata.csv',
        'fraud_detection/data/Transaction Data/transaction_records.csv'
    ])  # Populate with data from multiple CSV files
