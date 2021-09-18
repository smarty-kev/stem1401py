"""
Group Project with Guang Zhu and Zi Yue
1 : Kevin
2 : Guang Zhu
3 : Ze Yue
"""

# import random
import random



# all functions

# student ID
studentID_list = []

def generate_studentID():
    year = random.randrange(2018, 2021)
    number_sequence = random.randrange(3401, 5001)
    studentID = str(year) + str(number_sequence)
    while number_sequence in studentID_list:
        year = random.randrange(2018, 2021)
        number_sequence = random.randrange(3401, 5001)
        studentID = str(year) + str(number_sequence)
    # print(studentID, type(studentID))
    studentID_list.append(studentID)
    return studentID

# studentID = generate_studentID()
# studentID_list.append(studentID)


# first name

# alphabet
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
            "v", "w", "x", "y", "z")

def generate_fn():
    first_name = ""
    num_char = random.randrange(3, 11)
    a = 0
    for n in range(num_char):
        letter = random.choice(alphabet)
        if a == 0:
            letter = letter.capitalize()
        first_name += letter
        a += 1
    return first_name

# fn = generate_fn()
# print(fn)


# last name

def generate_ln():
    last_name = ""
    num_char = random.randrange(3, 11)
    a = 0
    for n in range(num_char):
        letter = random.choice(alphabet)
        if a == 0:
            letter = letter.capitalize()
        last_name += letter
        a += 1
    return last_name

# ln = generate_fn()
# print(ln)


# date of Birth

def generate_doB():
    year = random.randrange(1990, 2011)
    month = random.randrange(1, 13)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randrange(1, 32)
    elif year % 4 == 0 and month == 2:
        day = random.randrange(1, 30)
        if year % 100 == 0:
            if year % 400 != 0:
                day = random.randrange(1, 30)
            else:
                day = random.randrange(1, 29)
    else:
        day = random.randrange(1, 31)
    date_of_Birth = "{}-{:02}-{:02}".format(year, month, day)
    return date_of_Birth

# date_of_Birth = generate_doB()
# print(date_of_Birth)


# ClassNo

def generate_ClassNo():
    classes = ["C101", "C102", "C103", "C104", "C105",
               "C201", "C202", "C203", "C204", "C205",
               "C301", "C302", "C303", "C304", "C305",
               "C401", "C402", "C403", "C404", "C405",
               "C501", "C502", "C503", "C504", "C505"]
    ClassNo = random.choice(classes)
    return ClassNo

# ClassNo = generate_ClassNo()
# print(ClassNo)


# GPA

def generate_GPA():
    num1 = random.randrange(0, 5)
    num2 = random.randrange(0, 10)
    num3 = random.randrange(0, 10)
    GPA = f"{num1}.{num2}{num3}"
    return GPA

# GPA = generate_GPA()
# print(GPA)


# delete everything in File_CSV_1

def delete_all_File_CSV_1():
    csv_file = open("File_CSV_1.csv", "w")
    csv_file.truncate(0)

delete_all_File_CSV_1()

# open and create CSV

csv_file = open("File_CSV_1.csv", "a")

# note.txt
# my laptop couldn't run the loop 5000 times so I did 4800 times + 200 times
for t in range(5000):
    studentID = generate_studentID()
    studentID_list.append(studentID)
    fn = generate_fn()
    ln = generate_ln()
    doB = generate_doB()
    ClassNo = generate_ClassNo()
    GPA = generate_GPA()
    data = "{},fn-{},ln-{},{},{},{}\n".format(studentID, fn, ln, doB, ClassNo, GPA)
    csv_file.write(data)

csv_file.close()
