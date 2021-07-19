"""
encode()

string.encode(encoding='UTC-8', errors='strict')
"""

"""
encode()
The string encode() method returns encoded version of the given string.
string.encode(encoding='UTF-8',errors='strict')
"""
# Example 1
string = 'pythön!'
print('The string is:', string)
string_utf = string.encode()

print('The encoded version is:', string_utf)
print()

# Example 2
string = 'pythön!'
print('The string is:', string)

string_utf = string.encode(encoding='ascii', errors='ignore')
print('The encoded version is:', string_utf)

string_utf = string.encode(encoding='ascii', errors='replace')
print('The encoded version is:', string_utf)

# Example 3
string_utf = string.encode(encoding='UTF-8', errors='replace')
print('The encoded version is:', string_utf)
