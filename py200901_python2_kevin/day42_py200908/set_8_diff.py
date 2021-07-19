"""
set difference
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

result = A - B
print(result)

result = B - A
print(result)

result = A.difference(B)
print(result)

result = B.difference(A)
print(result)
