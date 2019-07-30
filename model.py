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

master = {}
accounts = {}

def load():
    global master
    with open(DATAPATH, "r") as accounts_json:
        master = json.load(accounts_json) ### error here 

def save():
    with open(DATAPATH, 'w') as file_object:
        json.dump(master, file_object, indent=2)

def create_account():
    print()
    print("First Name: ")
    accounts["First Name"] = input()
    print("Last Name: ")
    accounts["Last Name"] = input()
    print("Please enter a 4 digit PIN: ")
    accounts["pin"] = str(input())
    accounts["Balance"] = float(0)
    

def gen_account():
    ac_num = ''.join(str(random.randint(0,9)) for _ in range(5))
    ac_dict = {}
    ac_dict[ac_num] = None
    print("Your new account number is: " + ac_num)
    ac_dict.update(accounts)
    master.update(ac_dict)
    return master

def login_verify():
        account_num = input("Account Number: ")
        pin_verify = input("PIN: ")
        for account_num,pin_verify in master:
            if account_num in master and master[account_num]["pin"] == pin_verify:
                print('Login Successful') #could do a boolean and return true or false
        else:
                print("Login failed")

class Bankaccount:
    def __init__(self,id,pin,balance=0):
        self.id = id
        self.pin = pin
        self.balance = balance

    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        if self.balance - amount > 0:
                self.balance -= amount
        else:
                print("Insufficient Funds!")
 
    def deposit(self, amount):
        self.balance += amount