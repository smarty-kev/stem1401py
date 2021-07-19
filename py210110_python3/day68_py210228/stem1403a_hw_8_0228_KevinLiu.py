"""
[Homework]
2021-02-28
Show and Hide a label in a window
Due date: By the end of next Sat.
"""

# tkinter module
from tkinter import *


# hide label function
def hide(widget):
    return lambda: Pack.forget(widget)


# show label function
def show(widget):
    return lambda: widget.pack(side=LEFT)


# widget
root = Tk()
root.title('Python GUI - pack fill')
root.geometry('640x480+0+0')
root.config(bg='gray')


# labels
label1 = Label(root, text='Label 1', font=('Arial', 20), fg='red')
label2 = Label(root, text='Label 2', bg='black', fg="white", font=('Arial', 20))
label3 = Label(root, text='Label 3', font=('Arial', 20), fg='red')


# pack labels
label1.pack(side = LEFT)
label2.pack(side = LEFT)
label3.pack(side = LEFT)


# hide label
label1.after(2000, hide(label1))

# show label
label1.after(3000, show(label1))


root.mainloop()
