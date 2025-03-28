import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect('transactions.db')
    return conn

def create_table():
    """Create a table for storing transactions in SQLite."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            amount REAL,
            transaction_type TEXT,
            anomaly INTEGER
        )
    ''')
    conn.commit()
    conn.close()


    conn.commit()
    conn.close()

def insert_transaction(timestamp, amount, transaction_type, anomaly):
    """Insert a new transaction into the transactions table."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (timestamp, amount, transaction_type, anomaly)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, amount, transaction_type, anomaly))
    conn.commit()
    conn.close()

def fetch_transactions():
    """Fetch all transactions from the transactions table."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')

    rows = cursor.fetchall()
    conn.close()
    return rows
