"""
Recursion
is the process of defining something in terms of himself
1. example
2. example - recursive
"""

# 1X2X3X4X5

prod = 1

for i in range(1,6):
    prod = prod * i

# print(prod)


def f(n):
    if n == 1:
        return 1
    return n * f(n-1)


print(f(800))
