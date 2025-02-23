from collect_fee import SUBSCRIPTION_CONTRACT_ADDRESS
from config import INFURA_API_KEY
from web3 import Web3


w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"))


code = w3.eth.get_code(SUBSCRIPTION_CONTRACT_ADDRESS)
print(f"Connected: {w3.is_connected()}")
print(f"Current block: {w3.eth.block_number}")
