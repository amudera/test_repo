def logged_in():
    print()
    print("Hello, {}, {}".format(user, PIN)
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
         print("Your Balance is: {} ".format(balance))  

def withdraw():
        print()
        print("How much would you like to withdraw? ",end="")
        return input()

def deposit():
        print()
        print("How much would you like to deposit? ",end="")
        return input()

def insuff_funds():
        print()
        print("!!! INSUFFICIENT FUNDS !!!")