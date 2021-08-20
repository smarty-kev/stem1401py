"""
find all specified item from list
"""

my_list = ['p','r','o','b','l','e','m'] * 3

# to find letter of 'o'


# solution 1.
next_index = -1
for i in my_list:
    if i == 'o':
        next_index = my_list.index(i, next_index+1)
        print(next_index)
print()


# solution 2.
myindex = []
for index1 in range(len(my_list)):
    if my_list[index1] == 'o':
        # print(index)
        myindex.append(index1)

print(myindex)
print()


# solution 3
def getIndexOf(target):
    myindex = []
    for i in range(len(my_list)):
        if my_list[i] == target:
            # print(index)
            myindex.append(i)
    return myindex

target_index = getIndexOf('o')
print(target_index)
print()


# solution 4
def getIndexOf2(target):
    myindex = []
    next_index = -1
    for i in my_list:
        if i == target:
            next_index = my_list.index(i, next_index + 1)
            # print(next_index)
            myindex.append(next_index)
    return myindex

target_index = getIndexOf2('o')
print(target_index)


# Replace all
# find all -> replace all
# using function
# my_list = ['p','r','o','b','l','e','m'] * 3
def replaceall(target, new):
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm'] * 3
    next_index = -1
    for i in my_list:
        if i == target:
            next_index = my_list.index(i, next_index + 1)
            print(next_index)
            my_list[next_index] = new
    return my_list


my_list = replaceall('r', 'o')
print(my_list)