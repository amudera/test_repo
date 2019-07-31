#!/usr/bin/env python3

import model2
import view
from model2 import Bankaccount
bank = model2.Bankaccount()

def run():
    bank.load()
    view.main_menu()
    selection = view.get_input()
    mainmenu(selection)

def mainmenu(selection):
    while True:
        if selection == '3':
            bank.save()
            exit()
        elif selection == '1':
            firstname = view.First()
            lastname = view.Last()
            genpin = view.create_PIN()
            bank.create_account(firstname,lastname,genpin)
            bank.save()
            run()
        elif selection == '2':
            checkac = view.login_ac()
            checkpin = view.login_pin()
            if bank.login_verify(checkac,checkpin) == True:
                secondary() 
            else:
                run()
        else:
            view.bad_input()
            run()

def secondary():
    view.logged_in()
    selection2 = view.get_secondinput()
    secondmenu(selection2,bank)

def secondmenu(selection2,bank):
    while True:
        if selection2 == '4':
            bank.save()
            exit()
        elif selection2 == '1':
            balance = bank.getBalance()
            view.check_bal(balance)
            secondary()
        elif selection2 == '2':
            withdr = float(view.withdraw())
            bank.withdrawal(withdr)
            bal = bank.getBalance()
            view.new_bal(bal)
            bank.save()
            secondary()
        elif selection2 == '3':
            deps = float(view.deposit())
            bal = bank.depositor(deps)
            view.new_bal(bal)
            bank.save()
            secondary()
        else:
            view.bad_input()
            run()

if __name__ == "__main__":
    run()