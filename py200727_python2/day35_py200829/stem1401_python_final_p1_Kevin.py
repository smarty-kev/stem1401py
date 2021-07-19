"""
Program : remove punctuations
Author : Kevin
Date : 2020-08-29
"""

# explanation
print("This program removes any punctuations from the sentence you enter.")

# punctuations
punctuations = ["''","'","!","(",")","-","[","]","{","}",";",":","'"'"','"',"\\",",","<",">",".","/","?","@",\
    "#","$","%","^","&","*","~","'"]

# input
sentence = input("Please enter your sentence: ")


# echo sentence
for l in sentence:
    if l not in punctuations:
        print(l,end="")

# end
print("End of program")
