"""
Read a real .csv file know as data file
print out line by line
"""

def showdata(datalist):
    for entry in datalist:
        print(entry, end="") # without workshop_web_dec_2020 empty line

def showdatafield(entry):
    fields = entry.split()
    for field in fields:
        print(field)

# main program
# settings
DATA_FILE = "ect-Aug-2020-lower-level-data-release-csv.csv"

# data input
datalist = []

with open(DATA_FILE) as file:
    datalist = file.readlines()


# data processing
linenum = 1
entry1 = datalist[1]
showdatafield(entry1)

# data output
# showdata(datalist)

