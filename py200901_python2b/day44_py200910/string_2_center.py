"""
center()

string.center()
"""

# Example 1
string = "Python is awesome."
new_string = string.center(24)

print(f"Centered String: |{new_string}|")
print()

# Example 2
string = "Python is awesome"
new_string = string.center(24, '*')

print(f"Centered String: |{new_string}|")
print()

# Example 3
string = "Python is awesome "
new_string = string.center(24, '%')

print(f"Centered String: |{new_string}|")
print()
