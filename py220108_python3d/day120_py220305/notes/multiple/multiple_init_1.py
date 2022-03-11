"""

"""


class ParentA:
    def __init__(self):
        print("ParentA __init__() called.")


class ParentB:
    # not accessed
    def __init__(self):
        print("ParentB __init__() called.")


class Child(ParentA, ParentB):
    pass


# main
child1 = Child()
