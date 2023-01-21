from brownie import accounts, simpleStorage, config

def read_contract():
    #To get the address of the most recent deployed contract
    simple_storage = simpleStorage[-1]
    # Brownie already has our abi figured out so;
    print(simple_storage.retrieve())

def main():
    read_contract()