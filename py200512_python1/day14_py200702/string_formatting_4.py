"""
Number Formatting Types
Type	Meaning
d	Decimal integer
c	Corresponding Unicode character
b	Binary format
o	Octal format
x	Hexadecimal format (lower case)
X	Hexadecimal format (upper case)
n	Same as 'd'. Except it uses current locale setting for number separator
e	Exponential notation. (lowercase e)
E	Exponential notation (uppercase E)
f	Displays fixed point number (Default: 6)
F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
g	General format. Rounds number to p significant digits. (Default precision: 6)
G	Same as 'g'. Except switches to 'E' if the number is large.
%	Percentage. Multiples by 100 and puts % at the end.
"""

# d
n = 123
print("The number is {:3d}".format(n))

# n = 123.456
# print("The number is {:3d}".format(n))

# c
# char = "\u0039"
# print("The number is {:c}".format(char))

char = 65
print("The number is {:c}".format(char))

char = 97
print("The number is {:c}".format(char))

# b
b = 101
print("The number is b{:b}".format(b))

# o
o = 47
print("The number is 0o{:o}".format(o))

# x
x = 246
print("The number is 0x{:x}".format(x))

# X
x_uppercase = 76
print("The number is 0x{:X}".format(x_uppercase))

# n
n = 134596
print("The number is {:n}".format(n))

# e
e = 81
print("The number is {:e}".format(e))

# E
e = 978
print("The number is {:E}".format(e))

# f
f = 6567
print("The number is {:f}".format(f))

# F
f = 2378.32556234
print("The number is {:F}".format(f))

# g
g = 1895.8923456
print("The number is {:g}".format(g))

# G
g = 3123779.347721949
print("The number is {:G}".format(g))

# %
percentage = 0.178
print("The percentage is {:.2%}".format(percentage))
