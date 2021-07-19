"""
datatype conversion
"""

# case 1. str -> int
str1 = "1"
print(str1, type(str1))

c1 = int(str1)
print(c1, type(c1))

# case. 2 str -> float

str2 = "1.5"
print(str2, type(str2))

c2 = float(str2)
print(c2, type(c2))

# case. 3 int -> str

i3 = 100
print(i3, type(i3))

c3 = str(i3)
print(c3, type(i3))

# case. 4 float -> str

f4 = 100.12
print(f4, type(f4))

c4 = str(f4)
print(c4, type(c4))
