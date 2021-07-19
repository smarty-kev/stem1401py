"""
project : calculator
version : 2
"""

print("===Calculator===")
print("Please enter the corresponding number to the operation you want to select.")

# menu
menu = [1,2,3,4,5,6,7,8,9,10]
operation = ["Addition", "Subtraction", "Multiplication", "Division", "Floor Division", "Modulus", "Exponent", "Logical and", "Logical Or", "Logical Not"]

for i in range(1,len(menu)+1):
    print("{} {}".format(menu[i-1],operation[i-1]))

# functions


def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def mul(x,y):
    return x*y


def div(x,y):
    return x/y


def floordiv(x,y):
    return x//y


def mod(x,y):
    return x%y


def exp(x,y):
    return x**y


def logical_and(x,y):
    return x and y


def logical_or(x,y):
    return x or y


def logical_not(x):
    return not x


while 1:
    sel_ope = input("Operation [1-10], enter <<exit>> if you want to stop the program : ")
    if sel_ope == 'exit':
        break
    elif sel_ope == "1":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(add(x,y)))
    elif sel_ope == "2":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(sub(x,y)))
    elif sel_ope == "3":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(mul(x,y)))
    elif sel_ope == "4":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(div(x,y)))
    elif sel_ope == "5":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(floordiv(x,y)))
    elif sel_ope == "6":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(mod(x,y)))
    elif sel_ope == "7":
        print("You have selected {}".format(sel_ope))
        x = float(input("Enter the first operand : "))
        y = float(input("Enter the second operand : "))
        print("The result is {}.".format(exp(x,y)))
    elif sel_ope == "8":
        print("You have selected {}".format(sel_ope))
        x = input("Enter the first operand : ")
        y = input("Enter the second operand : ")
        if x == "True":
            x = True
        elif x == "False":
            x = False

        if y == "True":
            y = True
        elif y == "False":
            y = False
        print("The result is {}.".format(logical_and(x,y)))
    elif sel_ope == "9":
        print("You have selected {}".format(sel_ope))
        x = input("Enter the first operand : ")
        y = input("Enter the second operand : ")
        if x == "True":
            x = True
        elif x == "False":
            x = False

        if y == "True":
            y = True
        elif y == "False":
            y = False
        print("The result is {}.".format(logical_or(x,y)))
    elif sel_ope == "10":
        print("You have selected {}".format(sel_ope))
        x = input("Enter the first operand : ")
        if x == "True":
            x = True
        elif x == "False":
            x = False
        print("The result is {}.".format(logical_not(x)))
    else:
        print("Please select the a number from 1-10")

print("Good Bye!")
