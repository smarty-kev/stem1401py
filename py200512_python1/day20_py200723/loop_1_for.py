"""
for loop
"""

list1 = [1,2,3]

"""
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])
print(list1[9])
"""
# i : 0 -> 9
"""
for i in list1:
    print(i)

for item in list1:
    print(item)

# 1, 2, 3 .... 100
"""
"""
sum = 0
sum + 1 -> sum
sum + 2 -> sum
sum + 3 -> sum

sum + 100 -> sum
"""

# range(n) -> 0, 1, 2, 3, 4..... ,n-1
# range(1,101) -> 1,..... ,100
sum = 0
for i in range(1,101):
    print(i, end=",")
    sum = sum + i

print()
print("The sum of 1 to 100 is {}.".format(sum))
