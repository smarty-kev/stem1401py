"""
[Homework]
Date: 2021-05-09
Design and implement a multiple option button list on the main window.
Click on each button to show a specific toplevel window.
The number of options should be at list 5.
Due date: by the end of next Sat.
"""

# import module tkinter
from tkinter import *
import random


# functions
def open_new_window(category):
    new_window = Toplevel()
    new_window.title(category)
    new_window.config(bg=windows_bg[random.randint(0, 4)])
    new_window.mainloop()


# root window specifications
root = Tk()
root.title("Hw - Kevin | Toplevel")
root.geometry("+200+200")
root.config(bg="#ddddff")

# button 1-5
button_categories_names = ("Shop", "Account Balance", "Recent Purchases", "Settings", "Help")
windows_bg = ("#ddddff", "gold", "gray85", "darkblue", "pink")

column = 0
for name in button_categories_names:
    Button(root, text=name, width=13, height=3, bg="#ddddff", command=lambda category=name: open_new_window(category)).grid(padx=15, pady=75, row=0, column=column)
    column += 1


root.mainloop()
