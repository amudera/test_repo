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

def log_in():
    print()
    print("Account number: ")
    print("PIN: ")

def bad_input():
    print()
    print("ERROR! Incorrect iput ")

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
    
def check_bal():
         print()
         print("Your Balance is: {} ")

def withdraw():
        print()
        print("How much would you like to withdraw? ",end="")
        return input()

def deposit():
        print()
        print("How much would you like to deposit? ",end="")
        return input()