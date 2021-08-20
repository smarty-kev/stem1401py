"""
built-in

any() - Return true if any element of the set is true. If the set is empty, return False
"""

# case 1. empty set
s1 = set()
print(any(s1))

print()

# case 2. normal set
s2 = {False, False}
print(any(s2))

s2 = {True, True, True, False}
print(any(s2))

print()

# case 3.
s2 = {1, 0, 0, 0}
print(any(s2))

s2 = {1, 2, -1}
print(any(s2))

s2 = {1, 2, -1, 0}
print(any(s2))

s2 = {'a', 'b', ' '}
print(any(s2))

s2 = {'a', 'b', ''}
print(any(s2))
