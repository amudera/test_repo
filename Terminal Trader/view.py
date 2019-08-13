#!/usr/bin/env py

def welcome_screen():
        print()
        print("Trading Platform")
        print()
        print("1 Create Account")
        print("2 Log In")
        print("3 Quit")
        print()
        print("Please Pick an Option: ",end="")
        return input()

def improper_selection():
        print()
        print("Selction incorrect. Please try again")

def goodbye():
    print()    
    print("Goodbye!")
    quit()

def get_username():
    print()    
    return input("Please enter username: ")

def get_password():
    print()    
    return input("Please enter a 10 character max password: ")

def confirm_password():
        print()
        return input("Please confirm your passwordd: ")

def improper_password():
        print()
        print("Password Incorrect!")

def logged_in_screen():
    print()
    print("1 View Account and Positions")
    print("2 Deposit money")
    print("3 View Stock Price")
    print("4 Buy Stock")
    print("5 Sell Stock")
    print("6 Trade History")
    print("7 Log Out")
    print("8 Exit Application")

def account_positions(account):
        print()
        print("Your account is {}").format(account)

def show_positions(positions):
        print()
        print("Please see current positions below")
        return positions

def show_positions(trades):
        print()
        print("Please see trade history below")
        return trades

def trade_history():
        print()
        print("Please select Trade History Type")
        print()
        print("1 Stock Specific")
        print("2 All Trades")
        print()
        return input("Selection: ")

def buy_successful(amount,ticker):
        print()
        print("Trade Confirmed")
        print("BOUGHT {} SHARES OF {}").format(amount,ticker)

def sell_successful(amount,ticker):
        print()
        print("Trade Confirmed")
        print("SOLD {} SHARES OF {}").format(amount,ticker)

def add_balance():
        print()
        return input("Please add balance: ")

def improper_balance():
        print()
        print("Incorrect balance input")

def get_ticker():
        print()
        return input("Input Ticker Symbol: ")

def get_quantity():
        print()
        return input("Input Quantity: ")

def current_price(ticker,price):
        print()
        print("The price of {} is ${}").format(ticker,price)

def balance_error():
        print()
        print("Insufficient Funds to complete transaction")

def stock_error():
        print()
        print("Stock does not exist! Try Again")

def position_error():
        print()
        print("Position smaller than transaction size, cannot shortsell")

def no_position():
        print()
        print("You dont have a position in this stock")