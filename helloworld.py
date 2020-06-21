def registerUser():
    user = input("Input a username: ")
    password = input("Input a password: ")
    file = open("accounts.txt", "a")
    file.write(user)
    file.write(",")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are logged in.")
    else:
        print("Incorrect. Please try again.")


def login():
    user = input("Input a username: ")
    password = input("Input a password: ")
    for account in open("accounts.txt", "r").readlines():
        loginaccount = account.split(",")
        if user == loginaccount[0] and password ==loginaccount[1]:
            print("You are logged in.")
            return True
        else:
            print("Incorrect. Please try again.")
            return False

registerUser()
