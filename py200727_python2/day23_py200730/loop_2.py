"""
user is asked to input a number from 1 - 10
if the user failed to input a valid number
he/she will be asked to input again until he/she enters a valid number
"""



num = int(input("Please enter a number from 1 - 10: "))

while num < 1 or num > 10:
    num = int(input("Please re-enter a valid number from 1 - 10: "))

print("The number you input is {}".format(num))
