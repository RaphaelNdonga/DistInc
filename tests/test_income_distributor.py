from brownie import IncomeDistributor, accounts
from web3 import Web3


def test_add_shareHolders():
    incomeDistributor = IncomeDistributor.deploy({"from": accounts[0]})
    incomeDistributor.addShareHolder(accounts[0], 10)
    incomeDistributor.addShareHolder(accounts[1], 20)
    incomeDistributor.addShareHolder(accounts[2], 30)
    incomeDistributor.addShareHolder(accounts[3], 40)

    assert incomeDistributor.getShareHoldersArray(0) == accounts[0]
    assert incomeDistributor.getShareHoldersArray(1) == accounts[1]
    assert incomeDistributor.getShareHoldersArray(2) == accounts[2]
    assert incomeDistributor.getShareHoldersArray(3) == accounts[3]


def test_distributed_income():
    incomeDistributor = IncomeDistributor.deploy({"from": accounts[0]})
    incomeDistributor.addShareHolder(accounts[0], 10)

    sellingPrice = 1000

    incomeDistributor.sellItem({"from": accounts[0], "value": sellingPrice})

    assert incomeDistributor.getAmountFunded(accounts[0]) == 96
