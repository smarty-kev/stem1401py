"""

"""


class ParentA:
    def __init__(self):
        print("ParentA __init__() called.")


class ParentB:
    def __init__(self):
        print("ParentB __init__() called.")


class Child(ParentA, ParentB):
    def __init__(self):
        print("Child __init__() called.")


# main
child1 = Child()
