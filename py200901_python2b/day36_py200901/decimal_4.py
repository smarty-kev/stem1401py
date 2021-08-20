"""
getcintext()
"""

print(16.0/7)
# length of the decimal part
print(len(str(16.0/7))-2)\

from decimal import getcontext, Decimal

# set the precision
getcontext().prec = 3

output = Decimal(16.0)/Decimal(7)
print(output)

# to get the list of attributes or definition in a certain module
import decimal
# print(dir(decimal))

for i in dir(decimal):
    print(i)
