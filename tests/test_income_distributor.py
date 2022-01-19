from brownie import IncomeDistributor, accounts
from scripts.helpful_scripts import get_account
from web3 import Web3


def test_add_shareHolders():
    incomeDistributor = IncomeDistributor.deploy({"from": get_account()})
    incomeDistributor.createShareHolder(accounts[0], 10)
    incomeDistributor.createShareHolder(accounts[1], 20)
    incomeDistributor.createShareHolder(accounts[2], 30)
    incomeDistributor.createShareHolder(accounts[3], 40)

    assert incomeDistributor.getShareHoldersArray(0) == accounts[0]
    assert incomeDistributor.getShareHoldersArray(1) == accounts[1]
    assert incomeDistributor.getShareHoldersArray(2) == accounts[2]
    assert incomeDistributor.getShareHoldersArray(3) == accounts[3]


def test_distributed_income():
    incomeDistributor = IncomeDistributor.deploy({"from": get_account()})
    incomeDistributor.createShareHolder(accounts[0], 10)
    incomeDistributor.createShareHolder(accounts[1], 20)
    incomeDistributor.createShareHolder(accounts[2], 30)
    incomeDistributor.createShareHolder(accounts[3], 40)

    sellingPrice = 1000
    buyingPrice = incomeDistributor.getBuyingPrice()

    income = sellingPrice - buyingPrice

    incomeDistributor.sellItem({"from": get_account(), "value": sellingPrice})

    for i in range(incomeDistributor.getShareHoldersArraySize()):
        assert (
            incomeDistributor.getAmountFunded(accounts[i])
            == income * incomeDistributor.getShareHolderPercent(i) / 100
        )
