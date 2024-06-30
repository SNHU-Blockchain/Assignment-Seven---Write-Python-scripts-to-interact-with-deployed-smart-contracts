

from web3 import Web3
import requests

# Connect to a local Ethereum node
http_provider = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(http_provider))

# Debugging information
print(f"Connecting to Ethereum node at {http_provider}")

# Test the HTTP connection manually
try:
    response = requests.post(http_provider, json={"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1})
    if response.status_code == 200:
        print("HTTP connection to Ethereum node is successful.")
        print("Response:", response.json())
    else:
        print("HTTP connection to Ethereum node failed with status code:", response.status_code)
except Exception as e:
    print("HTTP connection to Ethereum node failed with exception:", str(e))

# Check if connected
try:
    if w3.is_connected():
        print("Connected to Ethereum node")
        # Get the latest block number
        latest_block = w3.eth.block_number
        print(f"Latest block number: {latest_block}")
    else:
        print("Failed to connect to Ethereum node")
except Exception as e:
    print("Error checking connection:", str(e))
