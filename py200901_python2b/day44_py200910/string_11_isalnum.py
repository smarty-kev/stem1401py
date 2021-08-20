"""
isalnum()

string.isalnum()
"""

# Example 1

name = "M234onica"
print(name.isalnum())

name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())

name = "Monica"
print(name.isalnum())

name = "Monica_122"
print(name.isalnum())
