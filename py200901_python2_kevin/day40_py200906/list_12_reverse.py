"""
list method: reverse()
list method: copy()
"""

my_list = ['p','r','o','b','l','e','m']


my_list.reverse()
print(my_list)


#
target = ['a','b','a']
print("target=", target)
new = target.copy()
new.reverse()
print("new=", new)

if new == target:
    print("Yes")
else:
    print("No")
