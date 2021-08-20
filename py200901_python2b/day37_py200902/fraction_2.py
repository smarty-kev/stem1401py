"""
converting a floating number to a fraction
"""

import fractions
import decimal

# ex1
print(fractions.Fraction(1.1))
print(decimal.Decimal(1.1))
print()

# solution 1. limit the denominator
result = fractions.Fraction(1.1).limit_denominator()
print(result)


# solution 2. as string
print(fractions.Fraction('1.1'))
