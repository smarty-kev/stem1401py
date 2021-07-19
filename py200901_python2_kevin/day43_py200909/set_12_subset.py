"""
set method

issubset()
"""
# case 1.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

is_subset = A.issubset(B)

if is_subset:
    print("A is a subset of B")
else:
    print("A is not a subset of B")
print()

# case 2.
A = {1, 2}
B = {1, 2, 3, 4, 5}

is_subset = A.issubset(B)

if is_subset:
    print("A is a subset of B")
else:
    print("A is not a subset of B")
print()

# case 3.
A = {1, 2, 8}
B = {1, 2, 3, 4, 5}

is_subset = A.issubset(B)

if is_subset:
    print("A is a subset of B")
else:
    print("A is not a subset of B")

