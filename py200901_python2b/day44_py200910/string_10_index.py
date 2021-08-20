"""
index()
"""

# Example 1.
sentence = 'Python programming is fun'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

# result = sentence.index('Java') -> ValueError: substring not found
# print("Substring 'Java':", result)

# Example 2.
sentence = 'Python programming is fun'
print(sentence.index('ing', 10))

print(sentence.index('g is', 10, -4))
# print(sentence.index('fun', 7, -8)) -> ValueError: substring not found
