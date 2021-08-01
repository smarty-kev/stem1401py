"""
[Homework]
Date: 2021-02-20
1. Write a GUI program of Label counter for implementing version 3.
Requirements:
(Function)
When the number reaches 10, then it comes to stop and displays the text of 'END'.
If a user clicks to close the main window, the program terminates.
(UI)
Using the layout manager of pack() for the UI.
A recommended UI design is given below.
Due date: by the end of next Friday
"""

from tkinter import *
from tkinter.ttk import Separator


step = 6


def run_counter(digit):
    """
    execute the counter and show current number on the Label
    :param digit: the label with which it display numbers
    :return:
    """
    def counting():
        global counter
        counter += 1

        if counter > step:
            counter = 0
            digit.config(text=counter)
            digit.after(1000, counting)
        else:
            digit.config(text=str(counter))
            digit.after(1000, counting)
    counting()


# main program
root = Tk()
root.title('Python GUI - Clock')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')


# title label
title_label = Label(root,
                    text = "Homework Clock",
                    bg = '#ddddff',
                    height = 1,
                    width = 30,
                    font = "Helvetic 12 bold")
title_label.pack(padx = 15, pady = 15)


# separator n.1
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)


# clock label
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 12,
              font = "Helvetic 35 bold")
digit_label.pack(padx = 15, pady = 15)


# separator n.2
sep2 = Separator(root, orient=HORIZONTAL)
sep2.pack(fill=X)

# footer
footer_label = Label(root,
                     text="Version 2, Kevin Liu, 1 August 2021",
                     bg = '#ddddff',
                     height=1,
                     width=30,
                     font="Helvetic 12 bold")
footer_label.pack(padx = 15, pady = 15)

# counting
counter = 0
run_counter(digit_label)
root.mainloop()
