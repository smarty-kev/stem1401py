"""
super and init

child overrides init() of parent and use its own init()

child has its own property: age
parent has no property.
"""


class Parent:
    def __init__(self):
        print('Parent __init__() called.')


class Child(Parent):
    def __init__(self, age):
        print('Child __init__() called.')
        self.age = age


# main
# c1 = Child()
# TypeError: __init__() missing 1 required positional argument: 'age'

c1 = Child(16)
print(c1.age)
