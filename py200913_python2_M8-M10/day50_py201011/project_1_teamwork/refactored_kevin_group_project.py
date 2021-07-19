"""
Group Project with Guang Zhu and Zi Yue
Author : Kevin Liu
This is the refactored code for the generating 5k records part of the project
"""

# import random
import random
# import string
import string


# all functions defining

# student ID (to avoid doubles)
studentID_list = []


def generate_studentID():
    year = random.randrange(2018, 2021)
    number_sequence = random.randrange(3401, 5001)
    studentID = str(year) + str(number_sequence)
    while number_sequence in studentID_list:
        year = random.randrange(2018, 2021)
        number_sequence = random.randrange(1, 5001)
        studentID = str(year) + str(number_sequence)
    studentID_list.append(studentID)
    return studentID


# generate 3 to 11 char (fn-name or ln-name)
def generate_name():
    name = ""
    num_char = random.randrange(3, 11)
    is_first_char = True
    for n in range(num_char):
        letter = random.choice(string.ascii_lowercase)
        if is_first_char:
            letter = letter.capitalize()
        name += letter
        is_first_char = False
    return name


# first name

def generate_fn():
    generate_name()
    first_name = generate_name()
    return first_name


# last name

def generate_ln():
    generate_name()
    last_name = generate_name()
    return last_name


# date of Birth

# all regular months (31 days months)
all_regular_months = [1, 3, 5, 7, 8, 10, 12]


# determinate the day (if it is 27, 28, 30 or 31)
def determine_leap_year(year, month):
    if month in all_regular_months:
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
    return day

# generate DoB
def generate_doB():
    year = random.randrange(1990, 2011)
    month = random.randrange(1, 13)
    day = determine_leap_year(year, month)
    date_of_Birth = "{}-{:02}-{:02}".format(year, month, day)
    return date_of_Birth


# ClassNo
def generate_ClassNo():
    ClassNo = "C" + str(random.randrange(1, 7)) + "0" + str(random.randrange(1, 7))
    return ClassNo


# GPA
def generate_GPA():
    GPA = round(random.uniform(0, 4), 2)
    return GPA


# delete everything in File_CSV_1

def delete_all_File_CSV_1(positive):
    if positive:
        csv_file = open("File_CSV_1.csv", "w")
        csv_file.truncate(0)


# you can turn this on (True) or off (False)
delete_all_File_CSV_1(True)


# main program

# open and create CSV

csv_file = open("File_CSV_1.csv", "a")

number_of_records_to_generate = 5000
for t in range(number_of_records_to_generate):
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
