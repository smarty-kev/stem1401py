"""
quiz 8 n. 8 - n. 10
"""

# n. 1
"""
+ , -, *, /, //, %, **
"""

# n. 2
"""
>, >=, <, <=, ==, !=
"""

# n. 3
"""
and, or, not
"""

# n. 4
"""
<<, >>, &, |, ~, ^
"""

# n. 5
"""
is, is not
"""

# n. 6
"""
in, not in
"""

# n. 7
"""
a = a + 1
"""

# n. 8
sentence = input("Please write down a sentence: ")
a = "a"
A = "A"
if (A or a) in sentence:
     print("True")
elif (A or a) not in sentence:
     print("False")


# n. 9
list1 = input("Please write down a list: ")
list2 = input("Please write down a list: ")
if list1 in list2 :
    print("They are identical")
elif list1 not in list2:
    print("They are not identical")


# n. 10
today = input("Please enter the number that is the date of the week: ")
result = (int(today) + 100)
print(result % 7)

# answer n. 8-9

# 8
sentence = input("Please write down a sentence: ")
a = "a"
A = "A"
if A in sentence or a in sentence:
     print("True")
elif A not in sentence or a not in sentence:
     print("False")

# 9

list1 = [1,2,3]
list2 = [1,2,3]

print("List1 is list2 {}".format(list1 is list2))

