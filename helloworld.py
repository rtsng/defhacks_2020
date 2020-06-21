def registerUser():
    user = input("Input a username: ")
    password = input("Input a password: ")
    file = open("accounts.txt", "a")
    file.write(user)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")


def login():
    user = input("Input a username: ")
    password = input("Input a password: ")
    for account in open("accounts.txt", "r").readlines():
        logininfo = account.split()
        if user == logininfo[0] and password ==logininfo[1]:
            print("You are now logged in.")
            return True
        else:
            print("Incorrect. Please try again.")
            return False

registerUser()
