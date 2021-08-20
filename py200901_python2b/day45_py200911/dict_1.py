"""
dictionary is a collection datatype
"""

# how to create a dictionary

dict1 = {
    1: "value1",
    2: "Value2",
    3: "value3",
    # ....
    1000: "value1000"
}

print(dict1)

# why
# every key in the dictionary will be hashable
# for look up a piece of data within a constant time
# iteration

for i in range(1000):
    print(i)

