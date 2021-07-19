"""
isdecimal()

string.isdecimal()
"""
# Example 1
s = "1234567"
print(s.isdecimal())

s = "32ladk3"
print(s.isdecimal())

s = "Mo3 nicaG el l22er"
print(s.isdecimal())

s = "1.23"
print(s.isdecimal())

s = "1.23e2"
print(s.isdecimal())
print()

# Example 2
# s = '²3455'
s = '\u00B23455'
print(s.isdecimal())
print('X\u00B2')

# s = '½'
s = '\u00BD'
print(s.isdecimal())
