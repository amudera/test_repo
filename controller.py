#!/usr/bin/env python3

import model
import view
from model import Bankaccount

def run():
    model.load()
    view.main_menu()
    selection = view.get_input()
    mainmenu(selection)

def mainmenu(selection):
    while True:
        if selection == '3':
            model.save()
            break
        elif selection == '1':
            model.create_account()
            model.gen_account()
            model.save()
            run()
        elif selection == '2':
            model.login_verify()
            if model.login_verify() == 'Login Successful':
                secondary()
            else:
                run()
        else:
            view.bad_input()
            run()

def secondary():
    view.logged_in()
    selection2 = view.get_secondinput()
    secondmenu(selection2)

def secondmenu(selection2):
    while True:
        if selection2 == '4':
            model.save()
            view.main_menu()
            return
        elif selection2 == '1':
            Bankaccount.getBalance()
        elif selection2 == '2':
            view.withdraw()
            Bankaccount.withdraw(view.withdraw())
        else:
            view.bad_input()

if __name__ == "__main__":
    run()