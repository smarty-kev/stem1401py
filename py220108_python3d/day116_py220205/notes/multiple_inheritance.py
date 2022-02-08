"""
multiple inheritance
"""


class ParentA:
    pass


class ParentB:
    pass


class Child(ParentA, ParentB):
    pass


class Child2(ParentB, ParentA):
    pass
