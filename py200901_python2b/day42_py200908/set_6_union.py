"""
set in mathematic
space of set (item)
universe

set operation

relationships of set
disjoint
joint/overlap
include
"""

# set union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
result = A | B
print(result)

result = A.union(B)
print(result)

result = B.union(A)
print(result)

C = {10, 11, 12}
result = A | B | C
print(result)
