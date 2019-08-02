#!/usr/bin/env python3

import json
import os
import random 
from random import randint
from random import seed
from collections import defaultdict

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH,DATA)

main = {}

def load():
    global main
    with open(DATAPATH, "r") as accounts_json:
        main = json.load(accounts_json) 

def save():
    with open(DATAPATH, 'w') as file_object:
        json.dump(main, file_object, indent=2)

def create_account(first1,last1,pin1):
    accounts = {"First Name:":first1,"Last Name:":last1,"pin":pin1,"Balance":float(0)}
    accounts.update()
    ac_num = ''.join(str(random.randint(0,9)) for _ in range(5))
    ac_dict = {}
    ac_dict[ac_num] = {}
    print("Your new account number is: " + ac_num)
    ac_dict[ac_num].update(accounts)
    main.update(ac_dict) 
    return main


def login_verify(account_num,pin_verify):
    if account_num in main and main[account_num]["pin"] == pin_verify: 
        return True
    else:
        return False

class Bankaccount:
    def __init__(self,balance=0):
        self.balance = balance
 
    def getBalance(self,main,ac_num):
        self.balance = main[ac_num]["Balance"]
        return self.balance
 
    def withdrawal(self, amount):
        if self.balance - amount > 0:
                self.balance -= amount
        else:
                print("Insufficient Funds!")
 
    def depositor(self, amount):
        self.balance += amount

