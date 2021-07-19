"""
datatype conversion
"""
# int -> str
n1 = 100
s1 = str(n1)
print(s1, type(s1))

# float -> str
f1 = 100.23
s2 = str(f1)
print(s2, type(s2))

# str -> int
int('1')
# int('1.2')

# str -> float
float('1')
print(f1, type(f1))

f1 = float('1.23')
print(f1, type(f1))