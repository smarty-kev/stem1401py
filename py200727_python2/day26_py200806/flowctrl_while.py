"""
while with condition at the top, in the middle, at the bottom
"""

# example 1.

sum = 0
i = 1

n = 10

while i < n:
    sum += i
    i += 1

# print("The sum is {}".format(sum))

# example 2.

vowels = 'aeiouAEIOU'

while 1:
    v = input("Enter a vowel: ")
    if v in vowels:
        break
    print("there is not a vowel. Try again")
print("Thank You!")


# example 3.

while True:
    a = int(input("Enter a number: "))
    print(a)
    if a == 0:
        break
