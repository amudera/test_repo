from unittest import TestCase
import sqlite3
from accounts_orm import Accounts
import os

filepath = "trader.db"

class TestAccounts(Testcase):

    def setup(self):
        username = "tbradley"
        password = "bearmarket2020"
        balance = 1000
        account = Accounts(username=username,balance=balance)
        account.set_password(password)
        account.generate_api_key()
        account.save()

    def testlogin(self,name,pword):
        test = Accounts()
        result = test.logincheck("afsdfsdf","dsfsdf")
        self.assertEqual(result,"Login Failed","Login Verification working")
    
    def testAPI(self,name,password): 
        user = Accounts("jblack")
        password = "jimmyblackout"
        balance = 500
        account = Accounts(username=username,balance=balance)
        account.set_password(password)
        new_api = account.generate_api_key()
        account.save()
        self.assertEqual()

    def test_balance(self,amount):
        tbrad = Accounts.login("tbradley","bearmarket2020")
        amount = 500
        update = Accounts.add_balance(amount)
        self.assertEqual(balance,1500,"Balance update worked")

