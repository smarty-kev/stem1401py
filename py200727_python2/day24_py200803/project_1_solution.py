"""
[Demo] Financial Statement
Data for Jan. 2020    ABC Bank

DATE       ENTITY             WITHDRAW   DEPOSIT    BALANCE
2020-01-30 SERVICE FEE        5.00                  ?
2020-01-25 INTEREST SURCHARGE 10.00                 ?
2020-01-20 RENTAL XYZ         1000.00               ?
2020-01-15 ROGERS             70.00                 ?
2020-01-10 CANADA GST                    500.00     ?
2020-01-05 RV QC  QST                    200.00     ?
2020-01-01 PROJECT MMM                   2000.00    ?
forward from 2019                                   1000.00
"""

"""
plan

1. choose a data structure to represent the data of the statement

2. calculate the balance and find a way using loop

3. output the financial statement with determined balance
"""

print("===FINANCIAL STATEMENT===")
print("Company: XYZ Inc.")
print("Period:   Jan-2020")
print("Date: August-03-2020")
print()

# 1.

# 2019
forward_balance = 1000.00

# DATE,ENTITY,WITHDRAW,DEPOSIT,BALANCE
trans = [["2020-01-01","PROJECT MMM",0,2000.0,0],
         ["2020-01-05","RV QC  QST",0,200.0,0],
         ["2020-01-10","CANADA GST",0,500.0,0],
         ["2020-01-15","ROGERS",70.0,0,0],
         ["2020-01-20","RENTAL XYZ",1000.0,0,0],
         ["2020-01-25","INTEREST SURCHARGE",10.0,0,0],
         ["2020-01-30","SERVICE FEE",5.0,0,0]]

print("===Original data===")
print("forward 2019 = {}".format(forward_balance))
print()


# 2.
# trial calculation
# print(trans[0])

for record in trans:
    forward_balance = forward_balance + record[3] - record[2]
    record[4] = forward_balance




# 3.

str_template = "{:^14} {:^20} {:^10} {:^10} {:^10}"

print(str_template.format("DATE","ENTITY","WITHDRAW","DEPOSIT","BALANCE"))

str_template = "{:14} {:20} {:10} {:10} {:10}"

for record in range(6,-1,-1):
    print(str_template.format(trans[record][0],trans[record][1],trans[record][2],trans[record][3],trans[record][4]))
print("forward from 2019","{:50}".format(1000.0))


"""
for i in range(6,-1,-1):
    forward_balance = forward_balance + trans[i][3] - trans[i][2]
    trans[i][4] = forward_balance
    print(str_template.format(trans[i][0],trans[i][1],trans[i][2],trans[i][3],forward_balance))
"""
