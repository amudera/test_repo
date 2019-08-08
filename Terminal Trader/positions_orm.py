import sqlite3

class Positions:
    dbpath = ""
    tablename = "positions"
    fields = ['ticker','quantity','price']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.ticker = kwargs.get("ticker")
        self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")

