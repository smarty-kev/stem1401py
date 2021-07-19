"""
project name : Loginform
version : 3
author : Kevin
date : August 10, 2020
"""

"""
plan:
1. create a username and store it as a variable
2. create a password and store it as a variable
3. authentication
"""

# A title or name of the application is required to show at first.
print("Welcome to Coding With Kevin")
print("=== Login Form ===")

# username
username = "Kevin"

# password
password = "12345"

# ask to input username
authentication_username = input("Please enter your username : ")

# ask to input password
authentication_password = input("Please enter your password : ")

# error count
error_count = 0


while authentication_username != username or authentication_password != password:
    # maximum number of tries
    error_count += 1
    if error_count == 6:
        print("Sorry, your account has been locked for security reasons.")
        break
    else:
        authentication_username = input("Please re-enter your username : ")
        authentication_password = input("Please enter your password : ")
else:
    # end
    print("Welcome {}! Your password is {}.".format(username,password))

    # goodbye
    print("Goodbye")
