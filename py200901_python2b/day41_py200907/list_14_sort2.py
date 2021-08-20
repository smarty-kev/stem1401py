"""
list sort
"""

# case 1. simple list
mylist = [1,5,3,5,3,5,6,7,8,9,0,2]

mylist.sort()
print(mylist)
print()

# case 2. nested list (matrix)
mylist2 = [[4, 'a'], [8, 'b'], [2, 'c'], [1, 'd']]
mylist2.sort()
print(mylist2)
print()

# case 3. sorting by specified column(key)
# solution 1
mylist2 = [[4, 'a'], [8, 'b'], [2, 'c'], [1, 'd']]
for i in mylist2:
    i.reverse()
print(mylist2)
mylist2.sort()
for i in mylist2:
    i.reverse()
print(mylist2)
print()

# solution 2 insert the target key to the first index
mylist3 = [[4, 10, 'a', 5], [8, 9, 'b', 4], [2, 8, 'c', 3], [1, 7, 'd', 0]]
for item in mylist3:
    item.insert(0, item[1])
    print(item)
mylist3.sort()

for item in mylist3:
    item.pop(0)
print(mylist3)
print()

# solution 3
mylist4 = [[4, 10, 'a', 5], [8, 9, 'b', 4], [2, 8, 'c', 3], [1, 7, 'd', 0]]

mylist4.sort(key=lambda item : item[2], reverse=True)
print(mylist4)
