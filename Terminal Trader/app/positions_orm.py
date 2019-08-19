import sqlite3
from orm import ORM
from util import get_price

class Positions(ORM):
    tablename = "positions"
    fields = ['ticker','quantity','price']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.accounts_pk = kwargs.get("accounts_pk")
        self.ticker = kwargs.get("ticker")
        self.quantity = kwargs.get("quantity")

    def current_value(self):
        price = get_price(self.ticker)
        value = price * self.quantity
        return value 

