"""
find()

str.find(sub[, start[, end]])
"""

# Example 1.
quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'let it':", result)

if "abc".find("z") != -1:
    print("Found")
else:
    print("Not Found")
print()

# Example 2.
quote = "Do small things with great love"
print(quote.find('small things', 10))
print(quote.find('small things', 2))
print(quote.find('o small', 10, -1))
