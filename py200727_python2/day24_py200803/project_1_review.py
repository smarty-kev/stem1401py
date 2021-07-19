"""
rewrite the project 1 print out financial statement
"""

print("===FINANCIAL STATEMENT===")
print("Company: XYZ Inc.")
print("Period:   Jan-2020")
print("Date: August-04-2020")
print()

balance = 1000.0

trans = [
         ["2020-01-01","PROJECT MMM",0,2000.0,0],
         ["2020-01-05","RV QC  QST",0,200.0,0],
         ["2020-01-10","CANADA GST",0,500.0,0],
         ["2020-01-15","ROGERS",70.0,0,0],
         ["2020-01-20","RENTAL XYZ",1000.0,0,0],
         ["2020-01-25","INTEREST SURCHARGE",10.0,0,0],
         ["2020-01-30","SERVICE FEE",5.0,0,0]
         ]

str_temp = "{:14} {:18} {:>10} {:>10} {:>10}"
print(str_temp.format("DATE","ENTITY","WITHDRAW","DEPOSIT","BALANCE"))

for i in trans:
    balance = balance + i[3] - i[2]
    i[4] = balance

for i in range(6,-1,-1):
    print(str_temp.format(trans[i][0],trans[i][1],trans[i][2],trans[i][3],trans[i][4],))
print("forward from 2019 {:48}".format(1000.0))