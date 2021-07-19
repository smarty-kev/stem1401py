"""
Checkbutton
get()
dictionary
variable, BooleanVar()
"""


from tkinter import *


def printInfo():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get():
            selection += roles[i] + "\t"
    print(selection)


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x120")

# label
labelframe = LabelFrame(root, text="Please choose your roles")
labelframe.pack()

# data, dictionary
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}
for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(labelframe, text=roles[i], variable=checkboxes[i]).pack()
Button(root, text="OK", width=10, command=printInfo).pack()

root.mainloop()
