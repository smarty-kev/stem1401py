"""
super and init

child directly inherits init() of parent

parameter: number of positional arguments must match
"""


class Parent:
    def __init__(self, name):
        print('Parent __init__() called.')
        self.name = name


class Child(Parent):
    pass


# main

# c1 = Child()
# TypeError: __init__() missing 1 required positional argument: 'name'

# must pass positional argument: name
c1 = Child('Peter')
