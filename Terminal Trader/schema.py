import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'trader.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS trader.db;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE accounts (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(10),
            password VARCHAR(10),
            balance FLOAT
        ); """
        cur.execute(SQL)

        
        SQL = "DROP TABLE IF EXISTS trader.db;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE positions (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            accounts_pk INT
            ticker VARCHAR(7),
            quantity INTEGER,
            price FLOAT
            FOREIGN KEY(accounts_pk,ticker) REFERENCES (accounts_pk),
            UNIQUE(accounts_pk,ticker)
        ); """
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS trader.db;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE trades (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            accounts_pk INT
            ticker VARCHAR(7),
            indicator TEXT,
            quantity INTEGER,
            price FLOAT
            time FLOAT
            FOREIGN KEY(accounts_pk) REFERENCES accounts(pk)
        ); """
        cur.execute(SQL)

if __name__ == "__main__":
    schema()