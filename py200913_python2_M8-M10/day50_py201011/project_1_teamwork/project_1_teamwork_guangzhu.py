"""
1:Kevin
2:Guang Zhu Cui
3:Ze Yue
"""
"""
Project:   Team Work
1. Each team member generate 5K entry of data
Description:
Generate a 5K lines of record and save them into a CSV file
Each entry should record such information as:
StudentID, First Name, Last Name, DateOfBirth, ClassNo, GPA
Sample:
20180001, fn-Bill, ln-Gates, 1995-03-05, C301, 3.3
Field Pattern
StudentID,     8-digit-number,    yyyy+4-digit sequence no,  20180001
                2018 to 2020, 0001 - 5000
First Name,        string of prefix + 3-10 characters,    'fn-' prefix + randomly generated
Last Name,     string of prefix + 3-10 characters,    'ln-' prefix + randomly generated
DateOfBirth,   string of 8 char,  yyyy-mm-dd,    2000-03-05
                the range of year 1990 - 2010
ClassNo,       C101, to C105, C201, to, C205 to C601 to C605, randomly generated
GPA,          0 to 4.0, randomly generated,       #.##,  #.#
Number of Records:
5,000 lines
Data File Format:
CSV
2. Each team member collects other two members' data file(s) in format of CSV
3. Calculate the GPA for every students and print out the report properly
export as a text file
summary
detail
4. Consider time management
schedule
meeting
"""

import random
import string


# student ID
def student_ID():
    stuid = []
    first_4_chars_student_id = str(random.randint(2018, 2020))
    last_4_chars_student_id = str(random.randint(1, 5000))
    stuid.append(last_4_chars_student_id)
    if last_4_chars_student_id in stuid:
        pass
    if len(last_4_chars_student_id) == 3:
        last_4_chars_student_id = '0' + last_4_chars_student_id
    if len(last_4_chars_student_id) == 2:
        last_4_chars_student_id = '00' + last_4_chars_student_id
    if len(last_4_chars_student_id) == 1:
        last_4_chars_student_id = '000' + last_4_chars_student_id
    student_id = first_4_chars_student_id.__add__(last_4_chars_student_id)
    return student_id


# first name
def fn():
    first_name = 'fn-'
    len_first_name = random.randint(3, 9)
    a = 0
    for i in range(len_first_name):
        first_char_fn = random.choice(string.ascii_uppercase)
        chars_fn = random.choice(string.ascii_lowercase)
        if a == 0:
            first_name += first_char_fn
        first_name += chars_fn
        a += 1
    return first_name


# last name
def ln():
    last_name = 'ln-'
    len_last_name = random.randint(3, 9)
    a = 0
    for i in range(len_last_name):
        first_char_ln = random.choice(string.ascii_uppercase)
        chars_ln = random.choice(string.ascii_lowercase)
        if a == 0:
            last_name += first_char_ln
        last_name += chars_ln
        a += 1
    return last_name


# birthdate
def date_of_birth():
    year = str(random.randint(1990, 2010))
    month = str(random.randint(1, 12))
    if month == '1' or month == '3' or month == '5' or month == '7' or month == '8' or month == '10' or month == '12':
        date = str(random.randint(1, 31))
    elif month == '2':
        date = str(random.randint(1, 28))
    else:
        date = str(random.randint(1, 30))
    if year == '1992' or year == '1996' or year == '2000' or year == '2004' or year == '2008' and month == '2':
        date = str(random.randint(1,29))
    if len(month) == 1:
        month = '0' + month
    if len(date) == 1:
        date = '0' + date
    birthdate = year + '-' + month + '-' + date
    return birthdate


# class NO
def class_no():
    class_number = 'C'
    first_number_in_the_class_number = str(random.randint(1, 5))
    last_number_in_the_class_number = str(random.randint(1, 5))
    class_number += first_number_in_the_class_number
    class_number += '0'
    class_number += last_number_in_the_class_number
    return class_number


# GPA
def GPA():
    gpa = round(random.uniform(0.1, 4.0), 2)
    return gpa


# main
try:
    csv_file = open('File_CSV_2.csv', 'w')
    csv_file.truncate(0)
    for i in range(1, 5001):
        a = '{},{},{},{},{},{}\n'.format(student_ID(), fn(), ln(), date_of_birth(), class_no(), GPA())
        csv_file.write(a)

except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    csv_file.close()

