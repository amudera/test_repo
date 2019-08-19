import sqlite3
from orm import ORM
from util import hash_password
from positions_orm import Positions
from util import get_price
from pprint import pprint
from trades_orm import Trades
import secrets

class Accounts(ORM):
    dbpath = ""
    tablename = "accounts"
    fields = ['username','password_hash','api_key','balance']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.username = kwargs.get("username")
        self.password_hash = kwargs.get("password_hash")
        self.api_key = kwargs.get("api_key")
        self.balance = kwargs.get("balance")

    # def new_account(self,username,password):
    #     username = input("Select Username: ")
    #     password = input("Select password: ")
    #     SQL = "INSERT INTO accounts (username, password, balance) VALUES (?,?,0)"
    #     with sqlite3.connect(self.dbpath) as conn:
    #         cur = conn.cursor()
    #         cur.execute(SQL,(username,password,0))
    #         results = cur.fetchall()
    #         pprint(results)
    
    # @classmethod
    # def logincheck(cls,name,pword):
    #     name = input("username: ")
    #     pword = input("password: ")
    #     SQL = "SELECT COUNT(*) FROM accounts WHERE username =? AND password = ?;".format(name,pword)
    #     with sqlite3.connect(cls.dbpath) as conn:
    #         cur = conn.cursor()
    #         cur.execute(SQL,(name,pword))
    #         results = cur.fetchall()
    #         if int(results[0][0]) == 0:
    #             print("Login Failed")
    #             quit()
    #         else:
    #             print("Login Successful")

    @classmethod
    def login(cls, username, password):
        return cls.one_from_where_clause("WHERE username=? AND password_hash=?",
                                            (username, hash_password(password)))
    @classmethod
    def api_authenticate(cls,api_key):
        return cls.one_from_where_clause(("WHERE api_key=?"),(api_key,))

    def generate_api_key(self):
        self.api_key = secrets.token_hex(40)
    
    def set_password(self, password):
        self.password_hash = hash_password(password)

    def get_position(self):
        return Positions.all_from_where_clause("WHERE accounts_pk=?",(self.pk,))

    def get_position_for(self,ticker):
        position = Positions.one_from_where_clause("WHERE ticker=? AND accounts_pk=?",(ticker,self.pk))
        if position is None:
            return Positions(ticker=ticker,accounts_pk=self.pk,shares=0)
        else:
            return position

    def get_trades(self):
        return Trades.all_from_where_clause("WHERE accounts_pk=? ORDER BY time=ASC",(self.pk,))

    def trades_for(self,ticker):
        trade = Trades.all_from_where_clause("WHERE ticker=? AND accounts_pk=? ORDER BY time=ASC",(ticker,self.pk))
        if trade is None:
            return None
        else:
            return trade 
    
    @classmethod
    def show_api(self):
        SQL = "SELECT api_key from accounts WHERE accounts_pk=?".format(self.pk)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()

            curs.execute(SQL)
            result = curs.fetchone()
            print(result)
        
    def buy(self,ticker,amount):
        position = self.get_position_for(ticker)
        price = get_price(ticker)
        if price is None:
            raise KeyError
        notional = price * amount
        trade = Trades(accounts_pk = self.pk, ticker=ticker,price=price,quantity=amount)
        if self.balance >= notional:
            self.balance -= notional
            trade.save()
            position.shares += int(amount)
            position.save()
            self.save()
        else:
            raise ValueError

    def sell(self,ticker,amount):
        position = self.get_position_for(ticker)
        price = get_price(ticker)
        if price is None:
            raise KeyError
        notional = abs(price * amount)
        trade = Trades(accounts_pk = self.pk, ticker=ticker,price=price,quantity=amount)
        if position.shares > amount:
            self.balance += notional
            trade.save()
            position.shares -= abs(int(amount))
            position.save()
            self.save()
        else:
            raise ValueError

    def add_balance(self,amount):
        if amount > 0:
            self.balance += amount 
            self.save()
        else:
            raise ValueError
    
    def view_balance(self,username,password):
        return 
            

            