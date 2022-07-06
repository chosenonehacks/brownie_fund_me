from logging.config import valid_ident
from os import access
from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
from tokenize import Funny
from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
        fund_me = FundMe[-1]
        account = get_account()
        entrance_fee = fund_me.getEnteranceFee()        
        print(f"the current entry fee is: {entrance_fee}")
        print("Funding")
        fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
        fund_me = FundMe[-1]
        account = get_account()
        fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()