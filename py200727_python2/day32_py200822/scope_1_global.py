"""
scope

type 1. global scope
type 2. local scope

global variable, global scope

local variable, local scope

"""


def foo1():
    b = 1
    pass


def foo2():
    """
    you can access (read) global variable inside a function
    :return:
    """
    print("inside foo2() a =",a)
    pass


# error
def foo3():
    """
    you cannot write (update) global variable inside a function
    :return:
    """
    # a = a + 1
    # a = 1
    pass


a = 1
print("in global scope a =",a)
foo2()


