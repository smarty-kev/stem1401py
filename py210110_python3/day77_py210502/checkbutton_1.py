"""
checkbutton widget
"""

from tkinter import *


def printInfo():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += roles[i] + "\t"
    print(selection)

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

label1 = Label(root, text="Choose your role",)
label1.pack()


roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}

checkboxes = {}

for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], variable=checkboxes[i]).pack()


# button
Button(root, text="OK", width=10, command=printInfo).pack()

# main program
root.mainloop()
