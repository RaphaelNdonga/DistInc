from brownie import IncomeDistributor
from scripts.helpful_scripts import get_account


def main():
    deploy_income_distributor()


def deploy_income_distributor():
    account = get_account()
    incomeDistributor = IncomeDistributor.deploy({"from": account})
    print("Contract deployed successfully!")
    print(f"Contract deployed to {incomeDistributor.address}")
    return incomeDistributor
