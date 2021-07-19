"""
file method writelines()

readlines()
    - built-in
    - user-defined function/method
    - third party methods

what object does this method belongs to?
    - find or create the object

result type?
    - primitive type(number, str) and collection type
    - other type with api?
    - other type convert to primitive type

processing data and manipulating data with logic
"""

file = open("mytext.txt", "w")
lines = ['as26fdsf\n', "12sada\n", "asqfa235ds\n"]
# lines = "asfqfeq"
file.writelines(lines)
file.close()

# conclusion
# case 1.
# lines = 'asdjkhjasf'
# writelines() can write a string directly

# case 2.
# lines = 'asdjkhjasf', "asdqfa", "asqfafhuihaf"
# writelines() accepts tuple

# case 3.
# lines = ['as26fdsf', "12sada", "asqfa235ds"]
# writelines() accepts list

# 4.
# clean/truncate and write

# 5.
# why the content are not written by line?
# append \n at the end of the line

'''
try:
    file = open("file_1_writelines.txt", "w+")
    content = """this is the new text to add
this is the new text to add
this is the new text to add\n"""
    print(type(file.readlines()))
    print(type(file.writelines(content)))
    result = str(file.writelines(content))
    print(result, type(result))
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    file.close()
'''
"""
d = {
    1: 11,
    2: 22
}

for v in d.values():
    print(v)

print(type(d.values()))
result = list(d.values())
print(result, type(result))
"""