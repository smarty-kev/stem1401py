"""
project : calculator
version : 3

to optimize (refine) the current program

refactor, refactoring
keep the features but making it cleaner
"""

print("===Calculator===")
print("Please enter the corresponding number to the operation you want to select.")

# menu
menu = [1,2,3,4,5,6,7,8,9,10]
operation = ["Addition", "Subtraction", "Multiplication", "Division", "Floor Division", "Modulus", "Exponent", "Logical and", "Logical Or", "Logical Not"]

# print menu
for i in range(0,len(menu)):
    print("{} : {}".format(menu[i],operation[i]))

# operations functions
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

# refactoring

def str1bool(x):
    if x == "True":
        x = True
    elif x == "False":
        x = False
    return x
def str2bool(y):
    if y == "True":
        y = True
    elif y == "False":
        y = False
    return y
def operand1input():
    x = float(input("Enter the first operand : "))
    return x
def operand2input():
    y = float(input("Enter the second operand : "))
    return y
def operand_boolean_x_input():
    x = input("Enter the first operand : ")
    return x
def operand_boolean_y_input():
    y = input("Enter the second operand : ")
    return y
def print_selection():
    print("You have selected {}".format(sel_ope))
def print_answer():
    print("The result is {}.".format(ope))

while 1:
    sel_ope = input("Operation [1-10], enter <<exit>> if you want to stop the program : ")
    if sel_ope == 'exit':
        break
    elif sel_ope == "1":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = add(x,y)
        print_answer()
    elif sel_ope == "2":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = sub(x,y)
        print_answer()
    elif sel_ope == "3":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = mul(x,y)
        print_answer()
    elif sel_ope == "4":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = div(x,y)
        print_answer()
    elif sel_ope == "5":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = floordiv(x,y)
        print_answer()
    elif sel_ope == "6":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = mod(x,y)
        print_answer()
    elif sel_ope == "7":
        print_selection()
        x = operand1input()
        y = operand2input()
        ope = exp(x,y)
        print_answer()
    elif sel_ope == "8":
        print_selection()
        x = operand_boolean_x_input()
        y = operand_boolean_y_input()
        x = str1bool(x)
        y = str2bool(y)
        ope = logical_and(x,y)
        print_answer()
    elif sel_ope == "9":
        print_selection()
        x = operand_boolean_x_input()
        y = operand_boolean_y_input()
        x = str1bool(x)
        y = str2bool(y)
        ope = logical_or(x,y)
        print_answer()
    elif sel_ope == "10":
        print_selection()
        x = operand_boolean_x_input()
        x = str1bool(x)
        ope = logical_not(x)
        print_answer()
    else:
        print("Please select the a number from 1-10")

print("Good Bye!")

