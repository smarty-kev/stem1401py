"""
Project1
Invoice_v1
Kevin
"""


# title
print("{:<40}{:>40}".format("East Repair Inc.","INVOICE"))


# line skip
print("{}".format(""))


# company information
print("{:<80}".format("1912 Harvest Lane"))
print("{:<80}".format("New York, NY 12210"))


# multiple line skip
print("{}{}{}{}".format("\n","\n","\n","\n"))


# client, shipment, invoice, and date information
str_struc = "{:<25}{:<25}{:>15}{:>15}" # string structure

a, b, c, d = "Bill To", "Ship to", "Invoice #", "US-001" # info
print(str_struc.format(a,b,c,d))

a, b, c, d = "John Smith", "John Smith", "Invoice Date", "11/02/2019" # info
print(str_struc.format(a,b,c,d))

a, b, c, d = "2 Court Square", "3787 Preview Drive", "P.O.#", "2312/2019" # info
print(str_struc.format(a,b,c,d))

a, b, c, d = "New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019" # info
print(str_struc.format(a,b,c,d))


# line break
print("{}".format(""))


# quantity, price and total information
str_struc = "{:^6}{:42}{:>15}{:>17}" # sting structure

a,b,c,d = "QTY","        DESCRIPTION","UNIT PRICE    ","AMOUNT    " # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "1","Front and rear brakes cables","100.00","100.00" # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "2","New set of pedal arms","15.00","30.00" # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "3","Labor 3hrs","5.00","15.00" # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "","","Subtotal","145.00" # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "","","Sales Tax 6.25%","9.06" # information
print(str_struc.format(a,b,c,d))

a,b,c,d = "","","TOTAL","154.06" # information
print(str_struc.format(a,b,c,d))


# 2 line break
print("{}".format("\n"))


# Terms and condition

str_struc = "{}" # string structure
print(str_struc.format("Terms and condition"))
print(str_struc.format("Payment is due within 15 days"))
print(str_struc.format(""))
print(str_struc.format("Please make checks payable to East Repair Inc."))


# end of the invoice
