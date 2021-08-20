"""
slicing

"""

# ex.
words = "Python is a good programming language."

words = ['P','y','t','h','o','n']

# case 1. slicing from the index of 0
print("=== Case 1 ===")
result = words[0:1]
print(result)

result = words[0:2]
print(result)

# exercise print P-h
result = words[0:4]
print(result)

result = words[:4]
print(result)

# case 2. slicing to the last index
print("=== Case 2 ===")
result = words[2:6]
print(result)

result = words[2:]
print(result)

# case 3. slicing from A to B
print("=== Case 3 ===")
result = words[2:4]
print(result)

# case 4. slicing all items
print("=== Case 3 ===")
result = words[0:len(words)]
print(result)

result = words[:]
print(result)
