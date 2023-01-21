from brownie import accounts, config, simpleStorage, network 

def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("goerli-testing")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # account2 = accounts[1]
    print(account)
    simple_storage = simpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(20, {"from": account})
    transaction.wait(1)
    updates_stored_value = simple_storage.retrieve()
    print(updates_stored_value)

def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



def main():
    deploy_simple_storage()