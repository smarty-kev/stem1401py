"""
string formatting
number formatting
"""

# example 1
# aligning to right by default for numbers
print("|{:5d}|".format(12))

# example 2
print("|{:2d}|".format(1234))

# example 3
print("|{:8.3f}|".format(12.2346))

# example 4
print("|{:05d}|".format(12))

# example 5
print("|{:08.3f}|".format(12.2346))