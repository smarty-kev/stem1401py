"""
list method
count()
"""

t1 = ('p','r','o','b','l','e','m') * 3

target = 'p'
result = t1.count(target)

# not recommended, magic value, magic number
# t1.count('p')

print(result)
