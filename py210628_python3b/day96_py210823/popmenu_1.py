"""
menu

basic menu and options
"""

from tkinter import *
from tkinter import messagebox


# fn
def Copy():
    print("Copy")


def Cut():
    print("Cut")


def Paste():
    print("Paste")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)
    # print(1)


root = Tk()
root.title("Popup Menu")
root.geometry("640x480+300+300")

# define menu and menu items
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Copy", command=Copy)
popupmenu.add_command(label="Cut", command=Cut)
popupmenu.add_separator()
popupmenu.add_command(label="Paste", command=Paste)


# set menu
root.config(menu=popupmenu)

root.bind("<Button-2>", showPopupMenu)


root.mainloop()
