"""

get the largest number and smallest number in the given list.
print out

"""

list1 = [2,3,4,5,6,3,2,1,3,5,6,7,5,3,5,5]

max_num = list1[0]

min_num = list1[0]


for i in list1:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print("The biggest number in the list is {}.".format(max_num))
print("The smallest number in the list is {}.".format(min_num))

