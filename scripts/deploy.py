from os import access
from re import L
from tkinter import TRUE
from brownie import FundMe, accounts, config, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIROMENTS

def deploy_fund_me():
    account = get_account()
    # mocks
    # pass the price feed address to our contract depengin on which network we are, if peristent network like rinkeby use address 
    # otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address,{"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")) #verifying scirpt on etherscan, requires export ETHERSCAN_TOKEN
    print(f"Contract deployed to {fund_me.address}")
    return fund_me



def main():
    deploy_fund_me()