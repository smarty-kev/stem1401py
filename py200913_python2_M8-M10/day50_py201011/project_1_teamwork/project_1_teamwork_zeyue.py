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

stuids = []

def generate():
    global stuids
    stuID = str(random.randint(2018, 2020)) + str(random.randint(1, 5)) + str(random.randint(0, 9)) \
            + str(random.randint(0, 9)) + str(random.randint(0, 9))
    while stuID in stuids:
        stuID = str(random.randint(2018, 2020)) + str(random.randint(1, 5)) + str(random.randint(0, 9)) \
                + str(random.randint(0, 9)) + str(random.randint(0, 9))
        if int(stuID[3:]) > 5000:
            stuID = stuID[0:3] + "5000"
    stuids += stuID
    firstname = "fn-"
    firstname += string.ascii_uppercase[random.randint(1, len(string.ascii_uppercase)-1)]
    for j in range(random.randint(2, 9)):
        firstname += string.ascii_lowercase[random.randint(1, len(string.ascii_lowercase)-1)]

    lastname = "ln-"
    lastname += string.ascii_uppercase[random.randint(1, len(string.ascii_uppercase)-1)]
    for j in range(random.randint(2, 9)):
        lastname += string.ascii_lowercase[random.randint(1, len(string.ascii_lowercase)-1)]

    dateOfBirth = str(random.randint(1990, 2010))
    m1 = str(random.randint(0, 1))
    if m1 == "1":
        m2 = str(random.randint(0, 2))
    else:
        m2 = str(random.randint(1, 9))
    dateOfBirth += "-" + m1 + m2

    d1 = str(random.randint(1, 2))
    if m1 + m2 == "02":
        if int(dateOfBirth[:3]) % 4 == 0:
            if int(dateOfBirth[:3]) % 100 != 0:
                d2 = str(random.randint(1, 9))
            elif int(dateOfBirth[:3]) % 100 == 0:
                d2 = str(random.randint(1, 9))
            else:
                d2 = str(random.randint(1, 8))
        else:
            d2 = str(random.randint(1, 8))
        day = d1 + d2
    else:
        if int(m1 + m2) < 8 and int(m1 + m2) % 2 != 0 or int(m1 + m2) > 7 and int(m1 + m2) % 2 == 0:
            day = str(random.randint(1, 31))
            if len(day) == 1:
                day = "0" + day
        else:
            day = str(random.randint(1, 30))
            if len(day) == 1:
                day = "0" + day
    dateOfBirth += "-" + day

    stuclass = "C" + str(random.randint(1, 6)) + "0" + str(random.randint(1, 5))

    gpa = round(random.uniform(0, 4), 2)

    return stuID + "," + firstname + "," + lastname + "," + dateOfBirth + "," + stuclass + "," + str(gpa)


f = open("File_CSV_3.csv", "w")
f.write("Student ID, First Name, Last Name, Date Of Birth, ClassNo, GPA\n")
for i in range(5000):
    line = generate()
    f.write(str(line) + "\n")
f.close()

