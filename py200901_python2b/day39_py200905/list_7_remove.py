"""
remove item(s) form a list

1. del keywords
2. clear()
3. remove()
4. pop()
"""

mylist = ['p','r','o','b','l','e','m']

# case 1. remove one item from a list
del mylist[2]
print(mylist)

# case 2. remove multiple items from a list
mylist = ['p','r','o','b','l','e','m']
del mylist[1:4]
print(mylist)

del mylist
# print(mylist)

# clear()
mylist = ['p','r','o','b','l','e','m']
mylist.clear()
print(mylist)

# remove()
mylist = ['p','r','o','b','l','e','m',]
mylist.remove('o')
print(mylist)

mylist = ['p','r','o','b','l','e','m','o']
mylist.remove('o')
print(mylist)
mylist.remove('o')
print(mylist)
# mylist.remove('o') -> ValueError: list.remove(x): x not in list
# print(mylist)


# pop(index)
mylist = ['p','r','o','b','l','e','m']
mylist.pop(0)
print(mylist)
# mylist.pop(10) -> IndexError: pop index out of range
# print(mylist)
