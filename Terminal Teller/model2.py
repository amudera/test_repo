#!/usr/bin/env python3

import json
import os
import random 
from random import randint
from random import seed
from collections import defaultdict

class Bankaccount:

    def __init__(self,ac_num="",balance=0.0):
        self.main = {}
        self.accounts = {}
        PATH = os.path.dirname(__file__)
        DATA = "data.json"
        self.DATAPATH = os.path.join(PATH,DATA)
        self.ac_num = ac_num
        self.balance = balance

    def load(self):
        with open(self.DATAPATH, "r") as file_object:
            self.main = json.load(file_object) 

    def save(self):
        with open(self.DATAPATH, "w") as file_object:
            json.dump(self.main, file_object, indent=2)
    
    def create_account(self,first1,last1,pin1):
        self.accounts = {"First Name:":first1,"Last Name:":last1,"pin":pin1,"Balance":float(0)}
        self.accounts.update()
        self.ac_num = ''.join(str(random.randint(0,9)) for _ in range(5))
        ac_dict = {}
        ac_dict[self.ac_num] = {}
        print("Your new account number is: " + ac_num)
        ac_dict[self.ac_num].update(self.accounts)
        self.main.update(ac_dict) 
        return self.main

    def login_verify(self,account_num,pin_verify):
        if account_num in self.main and self.main[account_num]["pin"] == pin_verify: 
            self.ac_num = account_num
            return True
        else:
            return False
 
    def getBalance(self): 
        self.balance = self.main[self.ac_num]["Balance"] 
        return self.balance
        
    def withdrawal(self, amount):
        self.balance = self.main[self.ac_num]["Balance"]
        if amount < self.balance:
            new_amt = self.balance - amount
            self.main[self.ac_num].update({"Balance":new_amt})
            return self.main[self.ac_num]["Balance"]
        else:
            print("Insufficient Funds!")
 
    def depositor(self, amount):
        self.balance = self.main[self.ac_num]["Balance"]
        if amount > 0:
            new_amount = self.balance + amount
            self.main[self.ac_num].update({"Balance": new_amount})
            return self.main[self.ac_num]["Balance"]
        else:
            print("Cant deposit a negative amount")

