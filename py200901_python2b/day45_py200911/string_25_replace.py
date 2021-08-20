"""
replace()
to replace a selected substring with a new one
"""

# to correct
str1 = 'Python is a good natural language'

# to replace 'natural' to 'programming'
str2 = str1.replace('natural', 'programming')
print(str2)


# to correct
str1 = 'Python is a good natural language. Java is also a good natural language.'

# to replace 'natural' to 'programming'
str2 = str1.replace('natural', 'programming')
print(str2)


# to replace with specified count
str2 = str1.replace('natural', 'programming', 1)
print(str2)
