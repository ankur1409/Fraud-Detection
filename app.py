from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load credit card data
def load_credit_card_data():
    credit_card_data = pd.read_csv('fraud_detection/data/creditcard.csv')
    return credit_card_data

@app.route('/')
def index():
    data = load_credit_card_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
