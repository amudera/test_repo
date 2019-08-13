import os
from orm import ORM
import controller
from util import set_token

DIR = os.path.dirname(__file__)
DBFILENAME = 'trader.db'
DBPATH = os.path.join(DIR,'data',DBFILENAME)

ORM.dbpath = DBPATH
controller.run()

util.set_token()

