"""
set
a set is:
~ collection of items
~ 1. unordered
~ 2. unique item (no duplicated item)
~ 3. set itself is mutable
~ 4. the item in a set is immutable
"""

# create an empty set
# set1 = {}
set1 = set()
print(set1, type(set1))

# create a normal set
set2 = {1, 2, 3}
print(set2, type(set2))

# create a set with duplicated items
set3 = {"EUROPE", "EUROPE", "STAY HOME", "ASIA", "ASIA", "ASIA"}
print(set3)

# unordered
set4 = {'a', 'b', 'c', 'd'}
print(set4)

# immutable items
# set5 = {1, 2, [4, 5, 6]} -> ->  TypeError: unhashable type: 'list'
# print(set5)

set5 = {1, 2, (5, 6)}
print(set5)

# set5 = {1, 2, {5 : 'a', 6 : 'b'}} ->  TypeError: unhashable type: 'dict'
# print(set5)

# application
"""
How many unique places did the student visit?
student:
A   US
B   EUROPE
C   ASIA
D   SOUTH AMERICA
E   AUSTRALIA
F   STAY HOME
G   US
H   EUROPE
I   US
J   STAY HOME
K   ASIA
"""

