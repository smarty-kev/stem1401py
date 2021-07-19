"""

"""


# import tkinter as tk
from tkinter import *


# function
def start_counting():
    print("entered start_counting()")

    global counter; counter += 1

    digit_label.config(text=counter)
    digit_label.after(1000, start_counting)


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
counter = 0
start_counting()


# mainloop
root.mainloop()
