import requests

APTOS_NODE_URL = "https://fullnode.testnet.aptoslabs.com"
MODULE_ADDRESS = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"  # Replace with your contract address

def get_reputation(user_address):
    url = f"{APTOS_NODE_URL}/v1/accounts/{user_address}/resource/{MODULE_ADDRESS}::Reputation::ReputationStore"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Reputation Score: {data['data']['reputation']}")
    else:
        print("Failed to fetch reputation score")

# Example Usage:
get_reputation("0xf8a2caaea2bfa3b9a1e68d882ad1b0f6f37e4d8cbbd65e3b1b35f5babeed1e78")
