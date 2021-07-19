"""
set method
copy()
"""

s1 = {1, 2, 3, 4, 5}

# write a program to clone a set (s2) based on s1
# to prove s2 is not identical to s1

s2 = s1.copy()
print(s2 is s1)

