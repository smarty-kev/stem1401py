"""
string formatting

"""

# example 1
# align to left by default for strings
print("|{:5}|".format("cat"))
print("|{:<5}|".format("cat"))
print("|{:*<5}|".format("cat"))

# example 2
print("|{:*>5}|".format("cat"))

# example 3
print("|{:^5}|".format("cat"))
print("|{:^6}|".format("cat"))

# example 4
print("|{:*^5}|".format("cat"))