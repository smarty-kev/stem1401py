"""
built-in function
enumerate() Return an enumerate object
It contains the index of the value of all items of set as a pair
"""

s1 = {"a", "b", "c"}

result = enumerate(s1)

# result = set(result)
result = list(result)
print(result)

# {(1, 'a'), (2, 'b'), (0, 'c')}
# {(1, 'c'), (0, 'b'), (2, 'a')}
# {(0, 'b'), (2, 'c'), (1, 'a')}

list1 = ["a", "b", "c"]

result = enumerate(list1)
result = list(result)
print(result)

# [(0, 'a'), (1, 'b'), (2, 'c')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
