"""
ex. 3
"""


list2 = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in list2:
    if i % 2 == 0:
        sum = sum + i


print("The answer is {}".format(sum))