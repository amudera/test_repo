import sqlite3

class Trades:
    dbpath = ""
    tablename = "trades"
    fields = ['ticker','indicator','quantity','price']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.ticker = kwargs.get("ticker")
        self.indicator = kwargs.get("indicator")
        self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")

 