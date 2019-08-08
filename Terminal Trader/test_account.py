import unittest
import sqlite3
from accounts_orm import Accounts


class TestAccounts(unittest.Testcase):

    def testlogin(self,name,pword):
        test = Accounts()
        result = test.logincheck("afsdfsdf","dsfsdf")
    
        self.assertEqual(result,"Login Failed","Login Verification working")