import model
import viewmain
import viewsecondary

def run():
    model.load()


def mainmenu():
    while True:
        viewmain.main_menu()
        selection = viewmain.get_input()
        if selection == '3':
            model.save()
            return
        elif selection == '1':
            newaccount = view.create_account()
            model.add_new_acc(account_number,PIN)
        elif selection == '2':
            