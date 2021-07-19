"""
get average
"""

mylist = [3,4,5,6,7,2,8,9]

sum = 0

i = 0

size = len(mylist)

while i < size:
    sum = sum + mylist[i]
    i = i + 1
avg = sum / size
print("the average is {}".format(avg))
