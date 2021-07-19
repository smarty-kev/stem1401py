"""
membership

in, not in

keywords : in, not
"""

# case 1 = list
list1 = [1,2,3,4,5,6,7]
print(8 in list1)

print(8 not in list1)

print(3 in list1)
print(3 not in list1)
print()

# case 2 = tuple
tuple1 = ('a','b','c','d')
print('b' in tuple1)
print('b' not in tuple1)
print()

print('z' in tuple1)
print('z' not in tuple1)
print()

# case 3 = set
set1 = {'pencil', 'eraser', 'crayons', 'sharpie'}
print('eraser' in set1)
print('eraser' not in set1)
print()

print('ruler' in set1)
print('ruler' not in set1)
print()

# case 4 = dictionary
dict1 = {
    "MON": "Monday",
    "TUE": "Tuesday",
    "WED": "Wednesday"
}

print('MON' in dict1)
print('MON' not in dict1)
print()

print('Monday' in dict1)
print('Monday' not in dict1)
print()
