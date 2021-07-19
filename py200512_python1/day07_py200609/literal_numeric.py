"""
Numeric literals
"""

"""
# integers
-1, -2, -3 ...
0
1, 2, 3, 4 ...
"""

"""
# floating number
ex : 1.1
     3.5
     100.55
     0.0
"""

# case 1.

d1 = 1
d2 = 10

# binary

b1 = 0b1
b2 = 0b10
b3 = 0b10110001010101010
print(b1)
print(b2)
print(b3)
# please write out binary number from 1 to 16
"""
0b1 = 1
0b10 = 2
0b11 = 3
0b100 = 4
0b101 = 5
0b110 = 6
0b111 = 7
0b1000 = 8
0b1001 = 9
0b1010 = 10
0b1011 = 11
0b1100 = 12
0b1101 = 13
0b1110 = 14
0b1111 = 15
0b10000 = 16
"""
# hexdecimal

h0 = 0x0
h1 = 0x1
h2 = 0x2
h3 = 0x3
h4 = 0x4
h5 = 0x5
h6 = 0x6
h7 = 0x7
h8 = 0x8
h9 = 0x9
h10 = 0xa
h11 = 0xb
h12 = 0xc
h13 = 0xd
h14 = 0xe
h15 = 0xf
h16 = 0x10

print(h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16)

# octal

o1 = 0o1
o2 = 0o2
o3 = 0o3
o4 = 0o4
o5 = 0o5
o6 = 0o6
o7 = 0o7
o8 = 0o10
print(o8)

# binary -> hex
b3 = 0b10110001010101010
print(hex(b3))
print(hex(150))

# hex -> binary

# binary -> octal
b3 = 0b10110001010101010
print(oct(b3))

# octal -> binary
o9 = 0o3456
print(bin(o9))

# decimal -> binary
