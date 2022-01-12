"""
[Homework]
v2
login form
"""

import os, time


class UserAccount:
    def __init__(self, name=None):
        self._name = name

    def login(self):
        global signed_in
        successful_login = False
        input_user = input("Your username? ")
        input_pass = input("Your password? ")
        for credential in credentials:
            credential = credential.split()
            if input_user == credential[0] and input_pass == credential[1]:
                successful_login = True
        if successful_login:
            self._name = input_user
            signed_in = True
            self.run_program()
        if not signed_in:
            print("Wrong credentials.")

    def logout(self):
        global signed_in
        if signed_in:
            signed_in = False
            print("Successfully logged out")
            print("Bye bye. Have a nice day.")
        elif not signed_in:
            print("Oops, you're not logged in.")

    def run_program(self):
        print(f"Welcome back, {self._name}!")
        print('\r' + "\\._./ you successfully logged in.", end="", flush=True)
        time.sleep(1)
        print('\r' + "\\>u</ you successfully logged in.", end="", flush=True)
        time.sleep(1)
        print("\n")

    @staticmethod
    def sign_up():
        username = input("Please enter your username: ")
        password = input("Please enter a strong password: ")
        date_of_birth = input("Please enter your birthday (yyyy/mm/dd): ")
        eula = "Please accept the terms and conditions (input 'yes'). For more information, visit 'info.com': "
        # end user licence agreement
        agreement = input(eula)
        if agreement == 'yes':
            file = open(file_name, 'a')
            content = f"{username} {password} {date_of_birth}\n"
            file.write(content)
            file.close()
            print("Nice, you have successfully created an account.")
            print("\n")
        else:
            print("Please try again and accept the terms and conditions of use and policy policies. Refresh the page. ")
        file = open(file_name, 'r')
        global credentials
        credentials = file.readlines()


# main program
# create a password file
file_name = 'credentials.txt'
if not os.path.isfile(file_name):
    f = open(file_name, 'w')


# account creation
new_user = False
if os.stat(file_name).st_size == 0:
    new_user = True

if new_user:
    print("Hello traveller, welcome to our website. Please create an account first.")
    UserAccount.sign_up()


# login
file = open(file_name, 'r')
credentials = file.readlines()
file.close()

signed_in = False
while 1:
    user = UserAccount()
    action = input("1 : Sign Up. 2 : Login. 3 : Logout. 4 : Exit program.\n")
    if action == "1":
        UserAccount.sign_up()
    if action == "2":
        user.login()
    if action == "3":
        user.logout()
    if action == "4":
        print("End of program.")
        break


