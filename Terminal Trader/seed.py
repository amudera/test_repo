import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'trader.db')

def seed(dbname=DBPATH):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        SQL = """INSERT INTO accounts (username, password, balance) VALUES (?, ?, ?)"""
        values = [("tbradley","TBRAD2019", 1000),
                ("jblack","jblackout32",500),
                ("mchen1992","Mendel92",100),
                ]
    
        cur.executemany(SQL,(values))

if __name__ == "__main__":
    seed()