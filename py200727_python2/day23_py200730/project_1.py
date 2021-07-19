"""
print out a financial statement
"""

# subject of document
print("[DEMO] Financial Statement")

# date and bank
print("Data for Jan. 2020 ABC Bank")

# blank line
print()

# starting balance
balance = 1000

# string template
str_template = "{:30} {:30} {:30} {:30} {:30}"

# the different dates
date = "2020-01-{}"
dates = ["forward from 2019",1,5,10,15,20,25,30]

# categories
columns_headers  = ["DATE   ","ENTITY    ","WITHDRAW  ","DEPOSIT  ","  BALANCE"]

# entities
entity = ["PROJECT MMM","RV QC","CANADA GST","RENTAL XYZ","INTEREST SUPERCHARGE","SERVICE FEE"]

# transactions
transactions = [1000,2000,200,500,-70,-1000,-10,-5]

matrix = [
    [dates],
    [entity],
    [transactions],
    [balance]
]

for i in range(len(columns_headers)):
    print(columns_headers[i],end="  ")
print()




