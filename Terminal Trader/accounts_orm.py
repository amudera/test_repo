import sqlite3
from pprint import pprint

class Accounts:
    dbpath = ""
    tablename = "accounts"
    fields = ['username','password','balance']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.balance = kwargs.get("balance")

    def new_account(self,username,password):
        username = input("Select Username: ")
        password = input("Select password: ")
        SQL = "INSERT INTO accounts (username, password, balance) VALUES (?,?,0)"
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            cur.execute(SQL,(username,password,0))
            results = cur.fetchall()
            pprint(results)
    
    @classmethod
    def logincheck(cls,name,pword):
        name = input("username: ")
        pword = input("password: ")
        SQL = "SELECT COUNT(*) FROM accounts WHERE username =? AND password = ?;".format(name,pword)
        with sqlite3.connect(cls.dbpath) as conn:
            cur = conn.cursor()
            cur.execute(SQL,(name,pword))
            results = cur.fetchall()
            if int(results[0][0]) == 0:
                print("Login Failed")
                quit()
            else:
                print("Login Successful")

            