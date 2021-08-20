"""
isprintable()
returns True if all characters in the string are printable or the string is empty.
If not, it returns False.
Characters that occupy printing space on the screen
are known as printable characters.
For example:
    letters and symbols
    digits
    punctuation
    whitespace
"""
"""
whitespace:  ' ', '\t', '\n'
"""
# Example 1
s = 'Space is a printable'
print(s)
print(s.isprintable())
s = '\nNew Line is printable'
print(s)
print(s.isprintable())
s = '\tTab is printable'
print(s)
print(s.isprintable())
s = ''
print('\nEmpty string printable?', s.isprintable())
print("==========\n\n")
# Example 2
s = chr(27) + chr(97)
print(chr(27))
print(chr(97))
if s.isprintable() == True:
    print('Printable')
else:
    print('Not Printable')
s = '2+2 = 4'
if s.isprintable() == True:
    print('Printable')
else:
    print('Not Printable')