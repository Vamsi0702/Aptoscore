import requests

# Aptos Testnet API Endpoint
API_URL = "https://fullnode.testnet.aptoslabs.com/v1"

# Your account address
account_address = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"

# Fetch last 10 transactions
response = requests.get(f"{API_URL}/accounts/{account_address}/transactions?limit=10")

# Check if request was successful
if response.status_code == 200:
    transactions = response.json()
    for txn in transactions:
        print(f"Txn Hash: {txn['hash']}, Success: {txn['success']}")
else:
    print("Error fetching transactions:", response.text)
