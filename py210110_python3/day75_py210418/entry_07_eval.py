"""
Entry
eval()
"""
from tkinter import *


def cal():
    out.configure(text="Result:  " + str(eval(equ.get())))


# main program
root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")
label = Label(root, text="Please input a math expression:")
label.pack()
equ = Entry(root)
equ.pack(padx=20, pady=5)
out = Label(root)
out.pack()
btn = Button(root, text="Calculate", command=cal)
btn.pack(pady=5)
root.mainloop()
