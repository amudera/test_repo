#!/usr/bin/env python3

import model
import view
from model import Bankaccount
bank = Bankaccount()

def run():
    model.load()
    view.main_menu()
    selection = view.get_input()
    mainmenu(selection)

def mainmenu(selection):
    while True:
        if selection == '3':
            model.save()
            break ### this is not exiting the program
        elif selection == '1':
            firstname = view.First()
            lastname = view.Last()
            genpin = view.create_PIN()
            model.create_account(firstname,lastname,genpin)
            model.save()
            run()
        elif selection == '2':
            checkac = view.login_ac()
            checkpin = view.login_pin()
            if model.login_verify(checkac,checkpin) == True:
                secondary() 
            else:
                run()
        else:
            view.bad_input()
            run()

def secondary():
    view.logged_in()
    selection2 = view.get_secondinput()
    bank = model.Bankaccount()
    secondmenu(selection2,bank)

def secondmenu(selection2,bank):
    while True:
        if selection2 == '4':
            model.save()
            run()
        elif selection2 == '1':
            bank.getBalance(main,ac_num)
        elif selection2 == '2':
            withdr = float(view.withdraw())
            bank.withdrawal(withdr)
            model.save()
            bank.getBalance()
            run()
        elif selection2 == '3':
            deps = float(view.deposit())
            bank.depositor(deps)
            model.save()
            bank.getBalance()
            run()
        else:
            view.bad_input()
            run()

if __name__ == "__main__":
    run()