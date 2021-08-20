"""
add item(s) to a set
add()
update()
"""

my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

# add more than one item
my_set = {1, 3}

# list
my_set.update([4, 5, 6])
print(my_set)

# tuple
my_set.update({10, 11})
print(my_set)

# set
my_set.update((7, 8, 9))
print(my_set)

# dict
my_set.update({12 : 'a', 13 : 'b'})
print(my_set)

# mix
my_set.update(('a', 'b'), ['c', 'd'])
print(my_set)
