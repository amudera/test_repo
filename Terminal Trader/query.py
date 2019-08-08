import sqlite3
import os
from pprint import pprint

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "trader.db"
DBPATH = os.path.join(DIRNAME, DBFILENAME)

def new_account():
    username = input("Select Username: ")
    password = input("Select password: ")
    SQL = "INSERT INTO accounts (username, password, balance) VALUES (?,?,0)"
    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cursor()
        cur.execute(SQL,(username,password,))
        

def query():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    name = input("username: ")
    pword = input("password: ")
    SQL = "SELECT COUNT(*) FROM accounts WHERE username = ? AND password = ?;"
    cur.execute(SQL,(name,pword))
    results = cur.fetchall()
    if int(results[0][0]) == 0:
        print("Login Failed")
        quit()
    else:
        print("Login Successful")

def checkbal():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    name = input("username: ")
    pword = input("password: ")
    SQL = "SELECT balance FROM accounts WHERE username = ? AND password = ?;"
    cur.execute(SQL,(name,pword))
    results = cur.fetchall()
    print(type(results))
    pprint(results)

checkbal()