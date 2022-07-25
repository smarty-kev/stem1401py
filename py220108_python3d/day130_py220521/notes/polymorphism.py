"""
OOP

polymorphism

method overload, overloaded methods
method override, overridden methods

int sum(a, b)
int sum(int, int)
int sum(float, float)
int sum(int, float)
int sum(float, int)

# no overloading
int sum1(int, int)
int sum2(float, float)
int sum3(int, float)
int sum4(float, int)

sum(1, 2)
sum(1.5, 2)
sum(1, 2.0)
sum(1.0, 2.0)


same structure -> multiple different results
"""


class A:
    def m1(self):
        pass


class B1(A):
    def m1(self):
        pass


class B2(A):
    def m1(self):
        pass


objectb1 = B1()
objectb1.m1()

objectb2 = B2()
objectb2.m1()

objecta = A()
objecta.m1()


def process(target_obj):
    target_obj.m1()


targetObj = objectb1
process(objectb1)
