const express = require('express');
const mongoose = require('mongoose');
const pd = require('pandas-js'); // Ensure pandas-js is imported

const app = express();
const PORT = process.env.PORT || 3100;

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/fraud_detection', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Middleware
app.use(express.json());
app.use(express.static(__dirname + '/public'));

// Transaction schema
const transactionSchema = new mongoose.Schema({
    timestamp: Date,
    amount: Number,
    transaction_type: String,
    anomaly: Boolean
});

const Transaction = mongoose.model('Transaction', transactionSchema);

// Route to save transaction data
app.post('/api/transactions', async (req, res) => {
    const transaction = new Transaction(req.body);
    await transaction.save();
    res.status(201).send(transaction);
});

// Route to get all transactions
app.get('/api/transactions', async (req, res) => {
    const transactions = await Transaction.find();
    res.send(transactions);
});

// Load credit card data
const load_credit_card_data = async () => {
    const credit_card_data = await pd.read_csv('fraud_detection/data/creditcard.csv');
    await Transaction.insertMany(credit_card_data.to_json(orient='records'));
};

// Load data when the server starts
load_credit_card_data().then(() => {
    app.listen(PORT, () => {
        console.log(`Server is running on http://localhost:${PORT}`);
    });
}).catch(err => {
    console.error('Error loading credit card data:', err);
});
