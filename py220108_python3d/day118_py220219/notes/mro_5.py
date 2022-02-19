"""
multiple inheritance
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class D2(C, B):
    pass


print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D2.__mro__)
# (<class '__main__.D2'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
