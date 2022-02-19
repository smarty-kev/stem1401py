"""
single inheritance
"""


class A:
    pass


class B(A):
    pass


print(B.__mro__)
# (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
