"""
4. Print out the data properly
"""

with open("CSV_file_Kevin.csv", "r") as csv_file:
    data = csv_file.readlines()
    # print(data)

for entry in data:
    print(entry, end="")

