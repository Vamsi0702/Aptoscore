from flask import Flask, jsonify, request
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Your Aptos account address
ACCOUNT_ADDRESS = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"
APTOS_NODE_URL = "https://fullnode.testnet.aptoslabs.com"

# Function to fetch transactions
def fetch_transactions(account, limit=50):
    url = f"{APTOS_NODE_URL}/v1/accounts/{account}/transactions?limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return []

# Process transactions into structured data
def process_transactions(transactions):
    print("Processing transactions...")
    data = []
    
    for txn in transactions:
        timestamp = int(txn.get("timestamp", 0))
        gas_used = int(txn.get("gas_used", 0))
        gas_price = int(txn.get("gas_unit_price", 0))
        success = 1 if txn.get("success", False) else 0  # Convert boolean to numeric

        data.append([timestamp, gas_used, gas_price, success])

    return pd.DataFrame(data, columns=["timestamp", "gas_used", "gas_price", "success"])


# Train ML model and predict reputation score
def train_and_predict(transaction_df):
    print("Training ML model and predicting reputation scores...")

    if len(transaction_df) < 5:
        print("Not enough transaction data to train the model. Using default reputation score = 50.")
        transaction_df["reputation_score"] = 50  # Assign default score for all transactions
        print(transaction_df)
        return transaction_df

    # Train the model
    X = transaction_df[["gas_used", "gas_price", "success"]]
    y = np.random.randint(50, 100, len(X))  # Fake labels

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    # Predict reputation scores
    transaction_df["reputation_score"] = model.predict(X_scaled)
    return transaction_df

@app.route('/get-reputation', methods=['GET'])
def get_reputation():
    transactions = fetch_transactions(ACCOUNT_ADDRESS, limit=100)
    
    if transactions:
        transaction_data = process_transactions(transactions)
        transaction_data = train_and_predict(transaction_data)
        return jsonify(transaction_data.to_dict(orient="records"))
    else:
        return jsonify({"error": "No transactions found for this account."})

if __name__ == '__main__':
    app.run(debug=True)
