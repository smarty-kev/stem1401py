"""
set method
isdisjoint()
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# write a program to clarify the relationship between a and b
relation = A.isdisjoint(B)

if relation:
    print("Set A and Set B are disjoint")
else:
    print("Set A and Set B are not disjoint")
