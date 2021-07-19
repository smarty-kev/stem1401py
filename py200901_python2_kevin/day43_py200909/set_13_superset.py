"""
set method

issuperset()
"""
# case 1.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

is_superset = A.issuperset(B)

if is_superset:
    print("A is a superset of B")
else:
    print("A is not a superset of B")
print()

# case 2.
A = {1, 2}
B = {1, 2, 3, 4, 5}

is_superset = A.issuperset(B)

if is_superset:
    print("A is a superset of B")
else:
    print("A is not a superset of B")
print()

# case 3.
A = {1, 2, 8}
B = {1, 2, 3, 4, 5}

is_superset = A.issuperset(B)

if is_superset:
    print("A is a superset of B")
else:
    print("A is not a superset of B")
