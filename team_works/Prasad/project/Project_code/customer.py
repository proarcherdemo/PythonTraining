
def new_user_registration():
    print("New User registration")
    f_name = input("Enter First Name : ")
    if len(f_name.strip())==0:
        print("Invalid First Name")
        return
    l_name = input("Enter Last Name : ")
    if len(l_name.strip())==0:
        print("Invalid Last Name")
        return
    dob = input("Enter DOB in DD/MM/YYYY format: ")
    if len(dob.strip())==0:
        print("Invalid Date of Birth")
        return
    adhar_num = input("Enter 12 digit adhar number :")
    if len(adhar_num)!=12:
        print("Please Enter 12 digit adhar number")
        return
    pan_num = input("Enter pancard number :")
    if len(pan_num)!=10:
        print("Please Enter 10 digit Pan number")
        return
    address = input("Enter address : ")
    if len(address.strip())==0:
        print("Invalid Address")
        return
    city = input("Enter city name : ")
    district = input("Enter district name : ")
    state = input("Enter state name : ")
    postal_code = input("Enter postal code : ")

    print("Your application has been sent to Admin successfully")



def login_screen():
    print("Please Enter User Id and Password for login")
    print("=================================")
    username = input("Enter Username : ")
    password = input("Enter password : ")

    if len(username.strip())==0:
        print("Invalid Username")
        return
    if len(password.strip())==0:
        print(("Invalid Password"))
        return
    print(username, password)





if __name__ == '__main__':
    print('*****Welcome to XYZ Bank*****')
    print('===========================================')
    print('1 New Account Creation')
    print('2 Existing User ? Login')

    user_choice = int(input("Please choose option 1 if you are new user else choose 2 for login into the application: "))

if user_choice ==1:
    new_user_registration()
elif user_choice==2:
    login_screen()