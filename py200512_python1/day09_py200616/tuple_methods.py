"""
tuple methods
"""
# count()
# tuple1 = (1,2,3,1,2,4,1,2,5,6,6,7,7,7)
tuple1 = "This is my project of python."
# count(1)      # error
# n1 = tuple1.count(1)    # correct way
# print("The number of 1 is {}".format(n1))
#
# n2 = tuple1.count(2)
# print("The number of 2 is {}".format(n2))
#
# n3 = tuple1.count(3)
# print("The number of 3 is {}".format(n3))
set1 = set(tuple1)
print(set1)
list1 = list(set1)
print(list1.sort())
for i in list1:
    n = tuple1.count(i)
    print("The number of {} is {}".format(i, n))
# count()
# tuple1 = (1,2,3,1,2,4,1,2,5,6,6,7,7,7)
tuple1 = "This is my project of python."
# count(1)      # error
# n1 = tuple1.count(1)    # correct way
# print("The number of 1 is {}".format(n1))
#
# n2 = tuple1.count(2)
# print("The number of 2 is {}".format(n2))
#
# n3 = tuple1.count(3)
# print("The number of 3 is {}".format(n3))
set1 = set(tuple1)
print(set1)
list1 = list(set1)
print(list1.sort())
for i in list1:
    n = tuple1.count(i)
    print("The number of {} is {}".format(i, n))