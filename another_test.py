
ACCOUNT_USERNAME = input("> ")
def stuff(ACCOUNT_USERNAME):
    if ACCOUNT_USERNAME.isalnum():
        print("special is absent")
    else:
        print("present")