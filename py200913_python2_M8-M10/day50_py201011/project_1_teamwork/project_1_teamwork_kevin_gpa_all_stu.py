"""
Calculate the gpa of every student (do average if the student appears in double)
"""

import csv

try:
    csv_1 = open("File_CSV_1.csv", "r")

    csv_1 = csv.reader(csv_1)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)


try:
    csv_2 = open("File_CSV_2.csv", "r")

    csv_2 = csv.reader(csv_2)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)


try:
    csv_3 = open("File_CSV_3.csv", "r")

    csv_3 = csv.reader(csv_3)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)

all_students_and_gpa = []
all_gpas = []

def get_all_students_and_gpa(datalist):
    field = 0
    for i in datalist:
        for l in i:
            if field == 1:
                all_students_and_gpa.append(l)
            if field == 2:
                all_students_and_gpa.append(l)
            if field == 5:
                all_students_and_gpa.append(l + "\n")
                try:
                    all_gpas.append(float(l))
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(e)
            field += 1
            if field == 6:
                field = 0

get_all_students_and_gpa(csv_1)
get_all_students_and_gpa(csv_2)
get_all_students_and_gpa(csv_3)



with open("student_and_gpa", "w") as summary_file:
    count = 0
    for i in all_students_and_gpa:
        if count == 2:
            summary_file.write(i)
        else:
            summary_file.write(i + ", ")
        count += 1
        if count == 3:
            count = 0
    total = 0
    for g in all_gpas:
        total += g
    average_gpa = total / len(all_gpas)
    summary_file.write(f"The average GPA of all the students is {average_gpa}")
