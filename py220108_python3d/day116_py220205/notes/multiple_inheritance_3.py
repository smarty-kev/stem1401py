"""
multiple inheritance
"""


class ParentA:
    def sing(self):
        print("sing()")


class ParentB:
    def painting(self):
        print("painting()")


class Child(ParentA, ParentB):
    pass


peter = Child()
peter.sing()
peter.painting()
