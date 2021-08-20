"""
[Homework]findAll  substring from a given string
"""

quote = 'let it be, let it be, let it be'

substr = 'let'

result = -1

while quote.find(substr, result + 1) != -1:
    result = quote.index(substr, result + 1)
    print(f"Substring {substr}:", result)
