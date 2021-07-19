"""
is -> collection datatype
"""

# collection datatype
# list, tuple, set, dict

# case 1
list1 = [1,2,3]
list2 = [1,2,3]

print(list1==list2)
print(list1 is list2)
print()

# case 2
tuple1 = (1,2,3)
tuple2 = (1,2,3)

print(tuple1==tuple2)
print(tuple1 is tuple2)
print()

# case 3
set1 = {1,3,6,4}
set2 = {1,3,6,4}

print(set1==set2)
print(set1 is set2)
print()

# case 4
dict1 = {
    "MON" : "Monday",
    "TUE" : "Tuesday",
    "WED" : "Wednesday"
}
dict2 = {
    "MON" : "Monday",
    "TUE" : "Tuesday",
    "WED" : "Wednesday"
}


print(dict1==dict2)
print(dict1 is dict2)
print()

print(dict1 is not dict2)