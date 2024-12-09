from handlers.loginhandler import LoginHandler

# Entry point of your application. Main script

def promptForLogin():
    print("Please enter you credentials to proceed further.")
    username = input("Username : ")    # user provided info
    password = input("Password : ")    # user provided info

    # Check if user and pass are not empty
    if len(username.strip()) == 0:
        print("Invalid Username")
        return
    if len(password.strip()) == 0:
        print("Invalid Password")
        return
    
    print(username, password)

    # Delegate the request to handler
    # Controller 
    response = LoginHandler.handle_login(username, password)


if __name__ == '__main__':
    print("\t\t\t\t\t\tWELCOME TO MY BANK")
    print("\t\t\t\t\t=================================")
    print("Kindly let us know how can we serve you !!! ")
    print("1. New Account Creation ")
    print("2. Existing user ? Login ")

    choice = int(input("Please enter your selection (1-2) : "))   # user provided choice
    
    if choice == 2:
        promptForLogin()


