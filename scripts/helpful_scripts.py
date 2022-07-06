from brownie import network, config, accounts, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development","ganache-local2"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS):
        return accounts[0]
    else:
        print (config["wallets"]["from_key"])
        return accounts.add(config["wallets"]["from_key"]) # config secion from brownie-config.yaml


def deploy_mocks():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:  
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"Active network is: {network.show_active()}")
        print(f"Deploying Mocks...")
        if len(MockV3Aggregator) <= 0: #if mock is alredy deployed then do nothing
            MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE, {"from": get_account()}) 
            print("Mocks deployed")