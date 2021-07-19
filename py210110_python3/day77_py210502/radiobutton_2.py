"""
radiobutton widget
"""

from tkinter import *


def printOption():
    print(roles[var.get()])


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

roles = {1:"Mage", 2:"Warrior", 3:"Archer"}
var = IntVar()
var.set(1)

# use selected option
label1 = Label(root, text="Your role",)
label1.pack()

for num, rolename in roles.items():
    Radiobutton(root, text=rolename, variable=var, value=num, command=printOption).pack()

# main program
root.mainloop()
