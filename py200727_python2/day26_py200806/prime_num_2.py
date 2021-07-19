"""
python program to print out all prime numbers in an interval

range(interval_
"""

# from 5 - 100, how many prime numbers are there and what are they

count = 0

start = int(input("Please enter the start number: "))
stop = int(input("Please enter the end number: "))

list1 = list(range(start,stop))
# print(list1)
"""
for n in list1:
    for i in range(2,n+1):
        if n % i == 0:
            break
        else:
            print(n)
            count += 1
            break
"""

true_false = True

for n in list1:
    for i in range(2,n+1):
        if n % i == 0 and n != i:
            true_false = False
            break
        else:
            true_false = True
    if true_false:
        print("{} is a prime number.".format(n))
        count += 1

print("There are {} prime numbers.".format(count))
