"""
1+2+3+4+....10
"""


def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


print(sum(998)) # max
