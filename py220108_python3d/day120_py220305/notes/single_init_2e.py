"""
super and init

child overrides init() of parent and use its own init()

child has its own property: age
"""


class Parent:
    def __init__(self, name):
        print('Parent __init__() called.')
        self.name = name


class Child(Parent):
    def __init__(self, age, name):
        print('Child __init__() called.')
        self.age = age
        super().__init__(name)


# main
# c1 = Child()
# TypeError: __init__() missing 1 required positional argument: 'age'

c1 = Child('peter', 18)

# order of arguments do not match that of the declared parameters
print(f"age: {c1.age}\nname: {c1.name}")
