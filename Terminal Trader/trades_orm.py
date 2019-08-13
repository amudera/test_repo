import sqlite3
from util import get_price
from orm import ORM
import time

class Trades(ORM):
    tablename = "trades"
    fields = ['accounts_pk','ticker','indicator','quantity','price']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk") 
        self.accounts_pk = kwargs.get('accounts_pk')
        self.ticker = kwargs.get("ticker")
        self.indicator = kwargs.get("indicator")
        self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")
        self.time = kwargs.get('time', time.time())

 