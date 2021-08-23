"""
menu

basic menu and options
"""

from tkinter import *
from tkinter import messagebox


# fn
def new():
    pass


def open():
    pass


def save():
    pass


def save_as():
    pass


def close():
    pass


root = Tk()
root.title("Menu")
root.geometry("640x480+300+300")

# define menu and menu items
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save as...", command=save_as)
file_menu.add_command(label="Close", command=root.destroy)


# set menu
root.config(menu=menu_bar)


root.mainloop()
