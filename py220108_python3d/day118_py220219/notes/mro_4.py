"""
multiple inheritance
"""


class A:
    pass


class B:
    pass


class C1(A, B):
    pass


class C2(B, A):
    pass


print(C1.__mro__)  # (<class '__main__.C1'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C2.__mro__)  # (<class '__main__.C2'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

