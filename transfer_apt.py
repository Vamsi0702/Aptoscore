import requests

# Replace with your details
SENDER_ADDRESS = "0xd39ca6e67a7b0dac1cbce4f42d8a8ea01edfe7d4ca25582ced8e0f8c63fdfd56"
PRIVATE_KEY = "0xd50ceabc010c1d620149043308e61cd023cea46969287a71ae1fc21ee9aeb332"  # You need this for signing transactions!
RECEIVER_ADDRESS = "0xf8a2caaea2bfa3b9a1e68d882ad1b0f6f37e4d8cbbd65e3b1b35f5babeed1e78"
APTOS_NODE_URL = "https://fullnode.testnet.aptoslabs.com/v1"

# Transaction payload
payload = {
    "sender": SENDER_ADDRESS,
    "sequence_number": "0",
    "max_gas_amount": "1000",
    "gas_unit_price": "1",
    "expiration_timestamp_secs": "9999999999",
    "payload": {
        "function": "0x1::coin::transfer",
        "type_arguments": ["0x1::aptos_coin::AptosCoin"],
        "arguments": [RECEIVER_ADDRESS, "1000000"]
    },
    "signature": {
        "type": "ed25519_signature",
        "public_key": "your-public-key-here",
        "signature": "your-signature-here"
    }
}

# Send the transaction
response = requests.post(f"{APTOS_NODE_URL}/transactions", json=payload)

# Print response
print(response.json())
