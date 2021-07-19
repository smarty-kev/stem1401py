"""
join()

returns a string by joining all the elements of an iterable,
separated by a string separator

string.join(iterable)

iterable = list, tuple, set, dictionary, string
"""

# Example 1. - list
mylist1 = ['a', 'b', 'c', '1', '2', '3']
sep = ','
result = sep.join(mylist1)
print(result, type(result))

mylist1 = ['Python', 'is', 'an', 'awesome', 'programming', 'language']
sep = ' '
result = sep.join(mylist1)
print(result, type(result))

sep = ''
result = sep.join(mylist1)
print(result, type(result))


# Example 4. string
s1 = 'abc'
s2 = '123'
print('s1.join(2):', s1.join(s2))

s1 = 'abc'
s2 = '123'
print('s1.join(2):', s1.join(s2))


# Example 5. dictionary
mydict = {'m' : 'monday', 't' : 'tuesday'}
sep = ','
print(sep.join(mydict))

# error
# mydict = {1 : 'monday', 2 : 'tuesday'}
# sep = ','
# print(sep.join(mydict))

mydict = {'1' : 'monday', '2' : 'tuesday'}
sep = ','
print(sep.join(mydict))
