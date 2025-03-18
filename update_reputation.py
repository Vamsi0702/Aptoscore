import requests
import json

APTOS_NODE_URL = "https://fullnode.testnet.aptoslabs.com"
PRIVATE_KEY = "0xd50ceabc010c1d620149043308e61cd023cea46969287a71ae1fc21ee9aeb332"  # Replace with your private key
SENDER_ADDRESS = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"  # Replace with your Aptos account address
MODULE_ADDRESS = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"  # Replace with contract address

def update_reputation(recipient, score):
    url = f"{APTOS_NODE_URL}/v1/transactions"
    
    payload = {
        "sender": SENDER_ADDRESS,
        "sequence_number": "0",
        "max_gas_amount": "1000",
        "gas_unit_price": "100",
        "expiration_timestamp_secs": "9999999999",
        "payload": {
            "function": f"{MODULE_ADDRESS}::Reputation::update_reputation",
            "type_arguments": [],
            "arguments": [recipient, str(score)]
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.json())

# Example Usage:
update_reputation("0xf8a2caaea2bfa3b9a1e68d882ad1b0f6f37e4d8cbbd65e3b1b35f5babeed1e78", 80)
