"""
list comprehension
"""

# case 1.
# [1,2,3,4,5] get a new list by doubling each item

# solution 1. for-loop
my_list = [1,2,3,4,5]
new_list = []
for i in my_list:
    new_list.append(i*2)
print(new_list)

# solution 2. map()
new_list = list(map(lambda item: 2*item, my_list))
print(new_list)


# solution 3. list comprehension
new_list = [item * 2 for item in my_list]
print(new_list)


# case 2. list comprehension + filter
# for, if, []
# [1,3,5,7,9]
new_list2 = [x for x in range(1,10) if x % 2 == 1]
print(new_list2)

