import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FraudDetectionModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01, random_state=42)

    def train(self, data):
        try:
            # Use all numeric columns for training
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            logger.info(f"Training with features: {numeric_cols.tolist()}")
            self.model.fit(data[numeric_cols])
        except Exception as e:
            logger.error(f"Error during training: {str(e)}")
            raise

    def predict(self, data):
        try:
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            return self.model.predict(data[numeric_cols])
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise

def load_data(file_path):
    """Load the creditcard.csv file"""
    try:
        logger.info(f"Loading data from {'creditcard.csv}")
        data = pd.read_csv('creditcard.csv')
        if data.empty:
            raise ValueError("Dataset is empty")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def preprocess_data(data):
    """Preprocess the data by dropping the 'isFraud' column and splitting into features and target"""
    X = data.drop('isFraud', axis=1)
    y = data['isFraud']
    return X, y

def evaluate_model(y_true, y_pred):
    """Evaluate the model's performance"""
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    matrix = confusion_matrix(y_true, y_pred)
    return accuracy, report, matrix

if __name__ == "__main__":
    try:
        # Load the data
        data = load_data('file_path')
        logger.info(f"Loaded data shape: {data.shape}")

        # Preprocess the data
        X, y = preprocess_data(data)
        logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the model
        model = FraudDetectionModel()
        model.train(X_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Convert predictions to binary labels (0: normal, 1: fraud)
        predictions_binary = [1 if prediction == -1 else 0 for prediction in predictions]

        # Evaluate the model's performance
        accuracy, report, matrix = evaluate_model(y_test, predictions_binary)

        # Print the results
        logger.info(f"Model Accuracy: {accuracy}")
        logger.info(f"Classification Report:\n{report}")
        logger.info(f"Confusion Matrix:\n{matrix}")

    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
