"""
diamond problem 2a
"""


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        A.m(self)


class C(A):
    def m(self):
        print("m of C called")
        A.m(self)


class D(B, C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)


# main
print(D.__mro__)

d1 = D()
d1.m()