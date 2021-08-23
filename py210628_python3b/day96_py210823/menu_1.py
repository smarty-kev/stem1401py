"""
menu

basic menu and options
"""

from tkinter import *
from tkinter import messagebox


# fn
def test_menu1():
    messagebox.showinfo("Test", "Menu 1 was clicked.")


def test_menu2():
    messagebox.showinfo("Test", "Menu 2 was clicked.")


root = Tk()
root.title("Menu")
root.geometry("640x480+300+300")

# define menu and menu items
menu_bar = Menu(root)
menu1 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="MENU_1", menu=menu1)
menu2 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="MENU_2", menu=menu2)
exitmenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Exit", menu=exitmenu, command=root.destroy)

root.config(menu=menu_bar)
root.mainloop()
root.mainloop()
