"""
ex. 4

how many times the number 2 is in the list1?

traversing
traversal

access: read and/or write
item/element:
"""

"""
list1 = [2,3,4,5,6,3,2,1,3,5,6,7]

number_of_twos = 0
for i in list1:
    if i * 2 - 4 == 0:
        number_of_twos = number_of_twos + 1

print("There is {} twos.".format(number_of_twos))
"""

list1 = [2,3,4,5,6,3,2,1,3,5,6,7]

num = int(input("Please enter a number: "))
number_of_num = 0
for i in list1:
    if i == num:
        number_of_num = number_of_num + 1

print("There is {} number of {}.".format(number_of_num, num))
