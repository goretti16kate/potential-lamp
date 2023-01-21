# import the compiler
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

# import json
import json

# import web3 for deployment
from web3 import Web3


load_dotenv()
# Read the file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile our contract
install_solc("0.8.17")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.17",
)
# print(compiled_sol)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["simpleStorage"]["evm"][
    "bytecode"
]["object"]

# get the abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["simpleStorage"]["abi"]


# In order to deploy to the mainet or testnet of your choice, you'll need to update the HTTPProvide, chain_id,
# private key and address

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/d569f665124846a79f18a078a9586f79"))
chain_id = 5
my_address = "0x6e7BaF181dEA284B99cC5a1A714Ca914006522eA"
private_key = os.getenv("PRIVATE_KEY")
print(private_key)

# Create the contract in python
simpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(simpleStorage)

# Get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = simpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# print(transaction)
# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)

# Send the signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# print(tx_hash)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Working with the contract
# 1. Contract Address
# 2. Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(simple_storage.functions.retrieve().call())

# Change the state of the blockchain
print("Building the Store Transaction......")
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
print("Signing the Store Transaction......")
## Sign the transaction
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
### Sending the signed transaction
print("Sending the signed transaction.....")
store_txn_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
print("Waiting for the Receipt......")
store_txn_receipt = w3.eth.wait_for_transaction_receipt(store_txn_hash)
print("Done¡¡¡¡¡¡")
print(simple_storage.functions.retrieve().call())
