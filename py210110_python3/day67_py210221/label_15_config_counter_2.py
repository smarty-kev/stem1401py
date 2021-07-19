"""
refactoring/optimize
"""


# import tkinter as tk
from tkinter import *


# function
def start_counting(mylabel):
    print("entered start_counting()")
    counter = 0

    def counting():
        nonlocal counter
        counter += 1

        mylabel.config(text=counter)
        mylabel.after(1000, counting)

    counting()


# main program
root = Tk()
root.title('Python GUI - Clock')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')


# label object
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 10,
              font = "Helvetic 30 bold")
digit_label.pack()


# start counting
start_counting(digit_label)


# mainloop
root.mainloop()
