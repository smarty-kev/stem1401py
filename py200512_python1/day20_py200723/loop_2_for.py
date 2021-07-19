"""
1,2,3,4,5,...20?
product = 1x2x3x4....x20
"""

product = 1
for i in range(1,21):
    product = product * i

print()
print("The product of 1 to 20 is {}.".format(product))