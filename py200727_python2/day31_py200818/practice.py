"""

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
