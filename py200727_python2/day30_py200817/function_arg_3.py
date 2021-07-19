"""
variable function arguments

2. Python keyword argument
"""


def greet(name="Bruce",msg="How do you do?"):
    print(f"{msg} {name}")


greet()
greet("Clark")
greet("Clark","Good morning!")
print()


def greet2(msg="How do you do?",name="Bruce"):
    print(f"{msg} {name}")


greet2()
greet2("Clark")
greet2("Clark","Good morning!")
greet2(name="Clark",msg="Good morning!")
# print()
