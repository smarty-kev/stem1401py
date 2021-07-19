"""
review of bitwise operators
"""

# &   Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x = 12
y = 13
print("x =",bin(x),"y =",bin(y))
result = x & y
print("x & y =", result)
print()

x = 5
y = 6
print("x =",bin(x),"y =",bin(y))
result = x & y
print("x & y =", result)
print()

# << This is the same as multiplying x by 2**y.
x = 12
y = 2
print("x =",bin(x),"y =",bin(y))
result = x << y
print("x << y =", result)
print()

x = 5
y = 3
print("x =",bin(x),"y =",bin(y))
result = x << y
print("x << y =", result)
print()

# >> This is the same as //'ing x by 2**y.
x = 12
y = 2
print("x =",bin(x),"y =",bin(y))
result = x >> y
print("x >> y =", result)
print()

x = 54
y = 3
print("x =",bin(x),"y =",bin(y))
result = x >> y
print("x >> y =", result)
print()

# |  Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
x = 12
y = 13
print("x =",bin(x),"y =",bin(y))
result = x | y
print("x | y =", result)
print()

x = 5
y = 6
print("x =",bin(x),"y =",bin(y))
result = x | y
print("x | y =", result)
print()

"""
# ^  Does a "bitwise exclusive or".
Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of
the bit in x if that bit in y is 1.
"""

x = 12
y = 13
print("x =",bin(x),"y =",bin(y))
result = x ^ y
print("x ^ y =", result)
print(bin(result))  
print()

x = 5
y = 6
print("x =",bin(x),"y =",bin(y))
result = x ^ y
print("x ^ y =", result)
print(bin(result))
print()

x = 78
y = 93
print("x =",bin(x),"y =",bin(y))
result = x ^ y
print("x ^ y =", result)
print(bin(result))
print()

"""
# ~  Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.
This is the same as -x - 1.
"""

x = 10
result = ~x
print(result)