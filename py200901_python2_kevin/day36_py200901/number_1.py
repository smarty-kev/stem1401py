"""
number data type in python

integer -> int (int, bin, hex, oct)
floating point -> float
complex numbers -> complex

Integers and floating points are separated by the presence of the absence of a decimal point
"""

"""
5    int
5.0  float
"""

"""
Decimal
"""

a = 1.1
b = 2.2
c = 3.3

print(a+b)
print(c)
print(a+b == c)

# 1.1 + 2.2 != 3.3
print("=== example 1 ===")
a = 1.1
b = 2.2
c = 3.3
print("a+b = ",a+b)
print("c = ",c)
print("a+b == c ?",a+b == c)
print("a+b > c ?",a+b > c)
print("a+b < c ?",a+b < c)
print()

# 3.3 == 3.3
d = 3.3
print("c == d?", c == d)
print("c is d?", c is d)
print()

# other example
print("=== example 2 ===")
f11 = 1.0
f12 = 0.1
f2 = 0.9
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

# other example
print("=== example 3 ===")
f11 = 1.0
f12 = 0.3
f2 = 0.7
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

# other example
print("=== example 4 ===")
f11 = 1.0
f12 = 0.33
f2 = 0.67
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()
