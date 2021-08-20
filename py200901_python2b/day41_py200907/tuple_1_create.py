"""
tuple

immutable ordered collection of items
"read-only list"
"""

# create an empty tuple
t1 = ()
print(t1, type(t1))

# create a normal tuple
t2 = (1,2,3,4)
print(t2, type(t2))


# to create a tuple with a single value
t3 = ('abc')
print(t3, type(t3))

t3 = ('abc',)
print(t3, type(t3))

# to create a tuple by tuple packing

t4 = 1, 2, 3, 4
print(t4, type(t4))

# auto-unpacking

a, b, c, d = t4
print(a, b, c, d)


# immutable
# item of mutable element can be changed
t5 = (1, 2, [3, 4], 'a')
# t5[0] = 111
# t5[1] = 111
# t5[2] = 111
t5[2][0] = 111
print(t5)

# tuple can be reassigned
t5 = (1, 2, 3)

# + operation
t6 = (1, 2, 3)
t7 = (4, 5, 6)
t8 = t6 + t7
print(t8, type(t8))

# * operation
t9 = t6 * 2
print(t9, type(t9))


