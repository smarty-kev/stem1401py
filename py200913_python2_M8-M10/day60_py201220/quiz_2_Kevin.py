"""
Part 2 q1 40 points, q2 10 points, q3 10 points
"""

import os, datetime, time, shutil


switch = True

shutil.rmtree("/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work")

# q1
print("==Start of q1 program==")

root_dir = "work"
os.mkdir(root_dir)  # create work directory

current_dir = "src"
os.mkdir(f"work{os.sep}{current_dir}")  # create src directory

n_files = int(input("Please enter the number of file you want to create: "))  # nb of files to create
name = input("Please enter the name of file\nAll files will have name_n: ")   # prefix of file


# create files
for n in range(n_files):
    file_with_ext = name + "_" + str(n+1) + ".txt"
    open(f"/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/src/{file_with_ext}", "x")
print("All files were created.")

new_dir = "dest"
os.mkdir(f"work{os.sep}{new_dir}")  # create dest directory

all_files_src = os.listdir("/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/src")
# print(all_files_src)

# main program
today = datetime.datetime.today()
# print(today)
for f in range(n_files):
    open(f"/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/dest/{all_files_src[f]}",
            "x")

for f in range(n_files):
    new_name = name + "_" + str(f + 1) + "_" + today.strftime("%Y-%m-%d")
    os.rename("/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/dest/" + all_files_src[f],
                "/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/dest/" + new_name + ".txt")

for f in range(n_files):
    os.remove("/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10/day60_py201220/work/src/" + all_files_src[f])
print("All files were copied to dest and renamed.")
print("===End of q1 program===")


# q2
print("==Start of q2 program==")
specified_location = input("Please enter the full path of directory which you want to list: ")
while not os.path.isdir(specified_location):
    print("No such directory")
    specified_location = input("Please enter the full path of directory which you want to list: ")


def list_all(dir, level=0):
    list_dir = os.listdir(dir)
    for name in list_dir:
        print(f"{'    ' * level}{name}")
        if os.path.isdir(dir+os.sep+name):
            level += 1
            list_all(dir+os.sep+name, level)
            level -= 1


list_all(specified_location)
print("===End of q2 program===")
time.sleep(3)

# q3
print("==Start of q3 program==")
print("The clock will continue as long as program is not terminated manually")
print("The directories and files created in q1 will also not be created until the program is terminated")
while True:
    print(f"\r{datetime.datetime.now().strftime('%I:%M %S %p')}", end="", flush=True)
    time.sleep(1)

