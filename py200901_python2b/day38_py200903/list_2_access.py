"""
accessing items or elements

indexing
by the index
"""

friends = ["Peter","Adam","Amy","Jack","Tom"]

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
# print(friends[5])
# IndexError: list index out of range

# to access an item in a nested list
mylist2 = [1,2,3,[4,5,6]]
# get the 5
i3 = mylist2[3]
print(i3)
print(i3[1])

print(mylist2[3][1])


# get the number of 23
matrix = [[11,12,13,14],
          [21,22,23,24],
          [31,32,33,34]]

print(matrix[1][2])

# application: to place a monster or item in a map
dataset = [
    [[1],[2],[3]],
    [[4],[5],[6]],
    [[7],[8],[9]],
]
print(dataset[1][1][0])

# negative index
# RTL starts from -1
friends = ["Peter","Adam","Amy","Jack","Tom"]
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[-4])
print(friends[-5])

# the first element
print(friends[0])


# the last element
print(friends[4])
print(friends[-1])

# len()

print("The length of the list is {}".format(len(friends)))
print(friends[len(friends)-1])
