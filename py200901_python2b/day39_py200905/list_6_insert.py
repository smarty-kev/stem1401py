"""
insert items to a list
"""

odd = [1,9]

# case 1. insert 1 item
odd.insert(1,3)
print(odd)

# case 2. insert 2 or more items
odd[2:2] = [5,7]
print(odd)

# ex.
student = ['Peter', 'Amy', 'Jack']
# please inset "Sarah" and "Tom" right after "Peter"
student[1:1] = ["Sarah","Tom"]
print(student)
