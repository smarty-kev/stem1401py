"""
arithmetic operation with fractions
comparison operation
"""

from fractions import Fraction as F

# ex1. addition and subtraction

result = F(1,3) + F(1,3)
print(result)


result = F(2,3) - F(1,6)
print(result)


# ex2.
result = 1/F(5,6)
print(result)


# ex3.
result = F(-3/10) > 0
print(result)


result = F(-3/10) < 0
print(result)
