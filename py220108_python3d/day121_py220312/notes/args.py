"""
*args
"""

print()
print("===========")

print(1)
print("===========")

print(1, 2)
print("===========")

print(1, 2, 3)
print("===========")


def foo(*args):
    for i in args:
        print(i)


foo('a', 'b', 'c')
