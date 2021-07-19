"""
number formatting with alignment
align to left
align to right
align to center
justified
"""

# example 1
print("|{:5d}|".format(12))
print("|{:>5d}|".format(12))

# example 2
print("|{:^5d}|".format(12))
print("|{:^6d}|".format(12))

# example 3
print("|{:<5d}|".format(12))

# example 4
print("|{:=8d}|".format(-12))
print("|{:=+8d}|".format(-12))