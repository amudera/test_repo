from accounts_orm import Accounts
import view
from util import get_price
import time

def run():
    welcome_menu()

def welcome_menu():
    while True:
        selection = view.welcome_screen()
        if selection not in ["1","2","3"]:
            view.improper_selection()
            continue

        if selection == '1':
            username = view.get_username()
            balance = view.add_balance()
            password = view.get_password()
            confirm_password = view.confirm_password()

            if password != confirm_password:
                view.improper_password()
                continue
            if not balance.isdigit() or int(balance) < 0:
                view.improper_balance()

            account = Accounts(username=username, balance=balance)
            account.set_password(password) 
            account.generate_api_key()
            account.save()
            logged_in_homepage(account)
            return

        elif selection == '2':
            username = view.get_username()
            password = view.get_password()
            logged_in_account = Accounts.login(username=username,password=password)
            if logged_in_account:
                logged_in_homepage(logged_in_account)
                return
            else:
                print("Invalid Credentials")
                continue

        elif selection == '3':
            view.goodbye()
            return

def logged_in_homepage(account):
    while True:
        selection = view.logged_in_screen(Accounts.username, Accounts.balance)
        if selection not in ["1","2","3","4","5","6","7","8","9"]:
            view.improper_selection()
            time.sleep(3)#delay codes execution by that many secs, waits 3 secs before executing next line of code
        
        if selection == '1':
            view.account_positions(Accounts.username)
            positions = Accounts.get_positions()
            view.show_positions(positions)
        
        elif selection == '2':
            amount = view.deposit_money()
            balance = Accounts.add_balance(amount)
            if balance == ValueError:
                view.improper_balance()
            else:
                view.deposit_successful()
            Accounts.save()
        
        elif selection == '3':
            ticker = view.get_ticker()
            view.current_price(ticker,get_price(ticker))
        
        elif selection == '4':
            ticker = view.get_ticker()
            amount = view.get_quantity()
            buy = Accounts.buy(ticker,amount)
            if buy == ValueError:
                view.balance_error()
            elif buy == KeyError:
                view.stock_error()
            else: 
                view.buy_successful(amount,ticker)     
            
        elif selection == '5':
            ticker = view.get_ticker()
            amount = view.get_quantity()
            sell = Accounts.sell(ticker,amount)
            if sell == ValueError:
                view.position_error()
            elif sell == KeyError:
                view.stock_error()
            else:
                view.sell_successful(amount,ticker)            

        elif selection == '6':
            select = view.trade_history()
            if select not in ["1","2"]:
                view.improper_selection()
                continue

            if select == "1":
                ticker = view.get_ticker()
                trade = Accounts.trade_for(ticker)
                if trade == None:
                    view.no_position()
                else:
                    return trade

            if select == "2":
                view.account_positions(Accounts.username)
                trades = Accounts.get_trades()
                view.show_trades(trades)

        elif selection == '7':
            view.api_key()
            Accounts.show_api()
        
        elif selection == '8':
            view.welcome_screen()

        elif selection == '9':
            quit()


if __name__ == "__main__":
    run()
