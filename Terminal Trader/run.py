import os
from app.orm import ORM
from app import controller
from app.util import set_token

DIR = os.path.dirname(__file__)
DBFILENAME = 'ttrader.db'
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

ORM.dbpath = DBPATH


controller.run()
