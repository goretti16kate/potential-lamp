from brownie import accounts, simpleStorage

def test_deploy():
    #Arrage
    account = accounts[0]
    #Act
    simple_storage = simpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    #Assert 
    assert starting_value == expected

def test_storage_update():
    #Arrage
    account = accounts[1]
    simple_storage = simpleStorage.deploy({"from": account})
    #Act
    expected = 68
    simple_storage.store(expected, {"from": account})
    #Assert

    assert expected == simple_storage.retrieve()