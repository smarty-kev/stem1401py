"""
remove items from a set
remove()
discard()
"""

s1 = {1, 3, 4, 5, 6}
print(s1)

# discard
s1.discard(4)
print(s1)

s1.discard(4)
print(s1)
print()

# remove()
s1 = {1, 3, 4, 5, 6}
print(s1)

s1.remove(4)
print(s1)

# s1.remove(4) -> KeyError: 4
# print(s1)

target = 8
if target in s1:
    s1.remove(target)

print(s1)
