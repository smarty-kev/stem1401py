"""
1,1,2,3,5,8,13,21,34,55...

the nth item of the sequence
f(1) = 1
f(2) = 1
f(3) = 2 = f(2) + f(1)
f(4) = 3 = f(3) + f(2)
f(5) = 5 = f(4) + f(3)
...
f(n) = ? = f(n-1) + f(n-2)
"""


def fib(pos):
    ib2 = 1
    ib1 = 0
    item = 0
    for pos in range(pos):
        item = ib1 + ib2
        ib2 = ib1
        ib1 = item
    return item


for x in range(1,11):
    print(fib(x),end=", ")
print()


# recursion
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n-1) + f(n-2)


print(f(5))
