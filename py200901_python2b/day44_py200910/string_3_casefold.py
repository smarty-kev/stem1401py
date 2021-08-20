"""
casefold() - aggressive lower() method

string.casefold()
lower() - turns upper case letter into lowercase letters
upper() -
"""

# Example 1
string = "PYTHON IS AWESOME"
new_string = string.casefold()

print("Lowercase string:", new_string)
print()

# Example 2
firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print("They are equal.")
else:
    print("They are not equal.")

# Example 3
firstString = "Der Fluß"
print(firstString.lower())

# Example 4
firstString = "der"
print(firstString.upper())
