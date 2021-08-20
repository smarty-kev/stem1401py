"""
add items to a list

append(item)

extend(item(s))

+ operator
* operator
"""

students = []

# on the 1st day
# students = ["Peter","Amy","Jack"]

students.append("Peter")
print(students)

students.append("Amy")
print(students)

students.append("Jack")
print(students)

# on the 2nd day
# Tom, Lily, Sarah, Amy
students.append("Tom")
print(students)
students.append("Lily")
print(students)
students.append("Sarah")
print(students)
students.append("Amy")
print(students)

# on the 3rd day
# Tom2 , Lily2, Sarah2, Amy2
students.extend(["Tom2","Lily2","Sarah2","Amy2"])
print(students)

# + operator
# concatenation (combining)
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list2+list1)

# * operator
print(list1 * 1)
print(list1 * 2)
print(list1 * 3)
print(list1 * 0)
print(list1 * -1)
print(list1 * -5)
