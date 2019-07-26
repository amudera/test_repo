import json
import os

PATH = os.path.dirname(__file__)
DATA = "dataset.json"
DATAPATH = os.path.join(PATH,DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)


def save():
    with open(DATAPATH, "w") as file_object:
        json.dump(data, file_object, indent=2)

#add account details to a dictionary
def add_new_acc():
    viewmain.log_in()