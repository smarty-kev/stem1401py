"""
istitle()
return True if string is only consisted of titlecased string
if not, return False

string.istitle()
"""

# Example 1
s = 'Python Is Good.'
print(s.istitle())
s = 'Python is good'
print(s.istitle())
s = 'This Is @ Symbol.'
print(s.istitle())
s = '99 Is A Number'
print(s.istitle())
s = 'PYTHON'
print(s.istitle())
s = 'PYTHON IS GOOD'
print(s.istitle())
