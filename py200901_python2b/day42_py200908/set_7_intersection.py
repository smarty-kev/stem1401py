"""
set intersection
"""

#   set intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

result = A & B
print(result)

result = A.intersection(B)
print(result)

result = B.intersection(A)
print(result)

C = {5, 11, 12}
result = A & B & C
print(result)
