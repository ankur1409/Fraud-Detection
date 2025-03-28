import pandas as pd
from sklearn.ensemble import IsolationForest

class FraudDetectionModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)  # Adjust contamination as needed

    def train(self, data):
        
        self.model.fit(data[['amount']])

    def predict(self, data):
       
        return self.model.predict(data[['amount']])

if __name__ == "__main__":
  
    data = pd.read_csv('fraud_detection/creditcard.csv') 

    model = FraudDetectionModel()
    model.train(data)
    predictions = model.predict(data)
    print(predictions)
