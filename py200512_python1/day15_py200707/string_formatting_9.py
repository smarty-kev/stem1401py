"""
truncating strings
"""

# example 1
# truncating
print("{}".format("caterpillar"))
print("{:.3}".format("caterpillar"))

# example 2
# padding
print("|{:5.3}|".format("caterpillar"))
# print("|{:5.3}|".format("caterpillar"))
print("|{:<5.3}|".format("caterpillar"))
print("|{:*<5.3}|".format("caterpillar"))

# example 3
print("|{:^5.3}|".format("caterpillar"))
print("|{:*^5.3}|".format("caterpillar"))