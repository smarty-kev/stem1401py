"""
hierarchical inheritance
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


print(B.__mro__)  # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

