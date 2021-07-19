"""
local variables and local scope

if we are using the same name of variables,

the one defined in local scope are not the ones defined in global scope
"""


def foo1():
    x = 1
    print(x, id(x))
    print("x inside foo1() is ", x)
    x = x + 2
    print("x inside foo1() is ", x)


x = 10
print(x, id(x))
print("x in global scope is",x)
foo1()
print("x in global scope is",x)

# we cannot access local variables outside function or in global scope
# print("can i access x inside a function?", x)
