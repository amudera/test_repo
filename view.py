#!/usr/bin/env python3

def main_menu():
    print()
    print("ATM Machine")
    print()
    print("1 Create Account")
    print("2 Log In")
    print("3 Quit")

def get_input():
    print()
    print("Please Pick an Option: ",end="")
    return input()

def First():
    return input("Please enter First Name: ")

def Last():
    return input("Please enter Last Name: ")

def create_PIN():
    return input("Please enter a new 4 digit PIN: ")

def login_ac():
    return input("Please enter your account number: ")

def login_pin():
    return input("Please enter your 4 Digit PIN: ")

def bad_input():
    print()
    print("ERROR! INCORRECT INPUT!")

def logged_in():
    print()
    print("1 Check Balance")
    print("2 Withdraw Funds")
    print("3 Deposit Funds")
    print("4 Sign Out")

def get_secondinput():
        print()
        print("Your choice: ",end="")
        return input()
    
def check_bal(balance):
         print()
         print("Your Balance is: {}".format(balance))

def new_bal(updated_balance):
         print()
         print("Your New Balance is: {}".format(updated_balance))

def withdraw():
        print()
        print("How much would you like to withdraw? ",end="")
        return input()

def deposit():
        print()
        print("How much would you like to deposit? ",end="")
        return input()