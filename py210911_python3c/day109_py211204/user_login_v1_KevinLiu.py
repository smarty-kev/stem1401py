"""
[Homework]
Date: 2021-12-04
Due date: 2021-12-10
1. Programming practice in OO
Project:	User Account and Login
Description:
A User has an account for a web application (such as google, youtube, amazon, etc.)
Users have to sign up before using the web app.
Users have to sign in each time to access web pages in the web app.
When a user signs up, he/she is asked to input username, password, date of birth and to check the checkbox of agreement of terms of use and privacy policies.
The system will store the credentials as well as other user info. into store media permanently.
After the user signs up, he/she then logins into the web app freely.
Each time the user must input username and password correctly, otherwise the system denies to pass.
When a user wants to exit from the web app, he/she can log out.
Requirement:
Creating a class named UserAccount
Finding attributes (or properties)
Finding methods
Concerning information hiding and encapsulation
Write a main program to create a user account for a user.
Let the user sign up.
Let the user sign in.
Let the user sign out.
"""

import os, time


class UserAccount:
    def __init__(self, username, password, date_of_birth):
        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth
        self.logged_in = False

    def login(self):
        input_user = input("Your username? ")
        input_pass = input("Your password? ")
        if input_user == self._username and input_pass == self._password:
            self.logged_in = True
        else:
            print("Wrong credentials, please refresh the page and try again.")
        if self.logged_in:
            self.run_program()

    def logout(self):
        self.logged_in = False
        print("Successfully logged out")
        print("Bye bye. Have a nice day.")

    def run_program(self):
        for i in range(3):
            print('\r' + "\\._./ you successfully logged in.", end="", flush=True)
            time.sleep(1)
            print('\r' + "\\>u</ you successfully logged in.", end="", flush=True)
            time.sleep(1)


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
    username = input("Please enter your username: ")
    password = input("Please enter a strong password: ")
    date_of_birth = input("Please enter your birthday: ")
    eula = "Please accept the terms and conditions (input 'yes'). For more information, visit 'info.com': "
    # end user licence agreement
    agreement = input(eula)
    if agreement == 'yes':
        file = open(file_name, 'w')
        content = f"{username} {password} {date_of_birth}"
        file.write(content)
        print("Nice, you have successfully created an account.")
        print("\n\n\n")
    else:
        print("Please try again and accept the terms and conditions of use and policy policies. Refresh the page. ")


# login
file = open(file_name, 'r')
credentials = file.read()
credentials = credentials.split()

user = UserAccount(credentials[0], credentials[1], credentials[2])
user.login()

while True:
    user_input = input("\nThe website has no feature for now :(. If you wish to exit, please enter 'logout': ")
    if user_input == 'logout':
        user.logout()
        break
