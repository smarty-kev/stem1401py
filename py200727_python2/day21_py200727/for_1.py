"""
for-loop
exercise
print a certain multiplication table
"""

string_template = "12 x {} = {}"

for i in range(1,11):
    print(string_template.format(i, 12 * i))