"""

"""


class A:
    def m(self):
        print("A.m()")


class B(A):
    def m(self):
        print("B.m()")


class C(A):
    def m(self):
        print("C.m()")


class D(B, C):
    pass


# test
d = D()
d.m()

