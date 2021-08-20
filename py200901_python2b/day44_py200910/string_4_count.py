"""
count()
"""

# Example 1
string = "Python is awesome, isn't it, is"
substring = "is"

count = string.count(substring)
print("The count is:", count)

# Example 2
string = "Python is awesome, isn't it, is"
substring = "is"

count = string.count(substring, 10)
print("The count is:", count)

# Example 3
string = "Python is awesome, isn't it, is"
substring = "is"

count = string.count(substring, 10, 21)
print("The count is:", count)
