"""
literal collection

collection - list
collection - tuple
collection - set
collection - dictionary
"""


# list
list_fruit = ['apple', 'peach', 'orange', 'pinaeapple']
list_stationary = ['pen', 'pencil', 'ruler', 'notebook', 'eraser']

print(list_fruit)
print(list_stationary)

fruits = ['apple', 'peach', 'orange', 'pinaeapple']

print(list_fruit[0])
list_fruit[0] = 'watermelon'
print(list_fruit[0])


# tuple
tuple_fruit = ('apple', 'peach', 'orange', 'pinaeapple')
tuple_fruit2 = ('orange', 'pinaeapple', 'apple', 'peach')
tuple_fruit3 = ('watermelon', 'peach', 'orange', 'pinaeapple', 'banana')

# tuple_fruit[0] = 'orange'
print(tuple_fruit[0])
print(tuple_fruit[1])
print(tuple_fruit[2])
print(tuple_fruit[3])

# set
# set is unordered
# items in a set must be unique

my_food = {'egg', 'milk', 'bread', 'ham', 'tomato'}
print(my_food)

my_number = {1,2,3,1,2,3}
print(my_number)

list_student = ["Cuba", "Colombia", "United-States", "Cuba", "Cuba", "Colombia", "France", "France"]

# how many places did the students go during spring break

set_places = {"Cuba", "Colombia", "United-States", "Cuba", "Cuba", "Colombia", "France", "France"}
print(set_places)

# dictionary
# dict
dict_day_of_week = {
    "MON" : "MONDAY",
    "TUE" : "TUESDAY",
    "WED" : "WEDNESDAY",
    "THU" : "THURSDAY",
    "FRI" : "FRIDAY",
    "SAT" : "SATURDAY",
    "SUN" : "SUNDAY",
}
print(dict_day_of_week)
print(dict_day_of_week["MON"])
