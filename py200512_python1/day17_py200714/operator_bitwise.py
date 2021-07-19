"""
bitwise operator
"""

# case 1. 4 bit number
# bit, binary number


x = 10
y = 4

print(bin(x))
print(bin(y))

# &
result = x & y
print("x & y =", result)

x = 9
y = 3
# x & y = ?
print("x =",bin(x))
print("y =",bin(y))
result = x & y
print("x & y =",result)


# |
x = 9
y = 3
# x | y = ?
result = x | y
print("x | y =", result)


# ~
x = 9
result = ~x
print(" ~x =", result)

# ^ XOR
x = 9
y = 4
# x ^ y = ?
result = x ^ y
print("x ^ y =", result)

# >>
x = 10
print("x >> =", x>>2)

# <<
x = 10
print("x << 1 =", x << 1)
print("x << 2 =", x << 2)
print("x << 3 =", x << 3)

#
x = x * 2
x *= 2
x << 2

#
