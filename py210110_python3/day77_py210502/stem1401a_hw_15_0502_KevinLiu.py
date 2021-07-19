"""
Date : 2021-05-02
Rewrite and try out Checkbutton
Understanding the sample code above
Due date: By the end of next Sat.
"""

from tkinter import *


def echo_selection():  # console
    selection = ""
    for item in checkboxes:
        if checkboxes[item].get():
            selection += roles[item] + "\t"
    print(selection)


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
# root.geometry("320x120")


# instruction - label
instruction = Label(root, text="Please choose your role (or roles)", bg="lightyellow")
instruction.grid(columnspan=3, pady=(10, 0))


# data for checkboxes (dictionary)
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}

checkboxes = {}

column = 0
for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], variable=checkboxes[i]).grid(column=column, pady=(10, 0), row=1)
    column += 1

# button - finish selection
Button(root, text="Done", width=10, command=echo_selection).grid(columnspan=3, pady=10)


root.mainloop()
