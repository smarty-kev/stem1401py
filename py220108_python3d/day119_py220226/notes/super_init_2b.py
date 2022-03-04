"""
super and init

child overrides init() of parent and use its own init()

no properties
"""


class Parent:
    def __init__(self):
        print('Parent __init__() called.')


class Child(Parent):
    def __init__(self):
        print('Child __init__() called.')


# main
c1 = Child()
