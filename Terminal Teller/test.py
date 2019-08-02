import json
import os
import random 
from random import seed
from random import randint

# PATH = os.path.dirname(__file__)
# DATA = "data.json"
# DATAPATH = os.path.join(PATH,DATA)

# accounts = {}

# def load():
#     global data
#     with open(DATAPATH, "r") as accounts_json:
#         data = json.load(accounts_json)


# def save():
#     with open(DATAPATH, "w") as accounts_json:
#        accounts_json.write(json.dump(accounts, indent=2))

# def create_account():
#     print()
#     print("First Name: ")
#     First = input("\n")
#     print("Last Name: ")
#     Last = input("\n")
#     print("PIN: ")
#     pin = str(input("\n"))
#     account_dict={"First Name":First,"Last Name":Last,"pin":pin}
#     return account_dict

# dict_ac = create_account()

# def gen_account():
#     ac_num = ''.join(str(random.randint(0,9)) for _ in range(5))
#     print("Your new account number is: " + ac_num)

# gen_account()

def gen_account():
    ac_num = ''.join(str(random.randint(0,9)) for _ in range(5))
    ac_dict = str(json.loads(ac_num))
    print(ac_dict)

gen_account()

        
  





