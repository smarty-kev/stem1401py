"""
list method - count()

Returns the count of number items passed in an argument
"""

my_list = ['p','r','o','b','l','e','m'] * 3


# how many times 'o' appears?

# solution 1
count = 0
target = 'o'
for l in my_list:
    if l == target:
        count += 1
print("The target of '{t}' occurs for {cnt} times.".format(t=target, cnt=count))


# solution 2
target = 'o'
cnt = my_list.count(target)
print("The target of '{t}' occurs for {cnt} times.".format(t=target, cnt=cnt))

# start 2
# cnt = my_list.count(target, 2)
# print("The target of '{t}' occurs for {cnt} times.".format(t=target, cnt=cnt))

