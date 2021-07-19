"""
variable function arguments

default argument

case 1. python default argument
"""


#
# def greet(greettings, friend):
#     print(f"{greettings}, {friend} !")

def greet(friend, greetings="Good morning"):
    print(f"{greetings}, {friend} !")

greet("Mary")
greet("Jack")
greet("Peter")

greet("Jack", "Good afternoon")

# ERROR
# def greet(greetings="Good morning",friend):
#     print(f"{greetings}, {friend} !")

# print("{0} {1} {2}".format(1,2,3))
# print("{0} {2} {1}".format(1,2,3))

# ERROR
# def greet(arg1,arg2,arg3,arg3="lol",arg4):
#     print(f"{greetings}, {friend} !")
