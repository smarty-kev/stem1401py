"""

"""


class A:
    def m(self):
        print("A.m()")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# test
d = D()
d.m()

