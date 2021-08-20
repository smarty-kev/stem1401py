"""
list

a collection type in python
list is a linear structure

list is ordered
list is mutable (changeable)

list can contain different data type of items
list can contain duplicated items

every item in a list has an index
"""

# example of single value v.s list
a = 1
b = [1]


# to create a normal list
friends = ["Peter","Adam","Amy","Jack","Tom"]
scores = [80, 96, 65, 89, 43]

profile_stu1 = ["2019090101","Peter","G8",14,80]

print(friends)
print(scores)
print(profile_stu1)


# to create an empty list
fruits = []
number = []

# fruits.append("apple")
# print(fruits)


# to create a nested list
mylist1 = [1,2,3,4,5,6]
mylist2 = [1,2,3,[4,5,6]]
print(mylist1)
print(mylist2)

mylist2 = [1,[7,8,9],3,[4,5,6]]
print(mylist2)

# how many items in mylist2

# how to create a matrix by 3X4
matrix = [[11,12,13,14],
          [21,22,23,24],
          [31,32,33,34]]
print(matrix)
