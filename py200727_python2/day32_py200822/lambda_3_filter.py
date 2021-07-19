"""
lambda function
filter()
"""

# 1, 2, 3, 4, 5, 6, .....
#


my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    if i % 2 == 0:
        print(i,end=", ")
print()


my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []

# result = filter(lambda x: x%2 == 0, my_list)
# print(result, type(result))

# result = list(result)
print(list(filter(lambda x: x%2 == 0, my_list)))
print()


# my_list = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda x: x%2 != 0, my_list)
# result = list(result)
print(list(filter(lambda x: x%2 != 0, my_list)))


# ex1
original = [1, 2, 3, 4, 5, 6]
target = [3, 5, 7, 9, 11, 13]

print(list(map(lambda x: 2 * x + 1, original)))
