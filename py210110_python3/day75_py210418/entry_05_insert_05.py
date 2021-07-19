"""
Entry
insert content where the cursor stays
position = INSERT
insert(INSERT, 'content')
"""
from tkinter import *


def printInfo():
    print(f"You've input: {entry1.get()}")


def insertInfoCursor():
    entry1.insert(INSERT, "-insert-")
    print(f"You've input: {entry1.get()}")


def insertInfoEnd():
    entry1.insert(END, "-insert-")
    print(f"You've input: {entry1.get()}")


def insertInfoHead():
    entry1.insert(0, "-insert-")
    print(f"You've input: {entry1.get()}")


# def clearInfo():
#     entry1.delete(0,END)
root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")
accountL = Label(root, text="Input ")
accountL.grid(row=2, padx=(50, 5), sticky='e')
entry1 = Entry(root)
entry1.grid(row=2, column=1, padx=(5, 50), columnspan=3)
printbtn = Button(root, text="Print", command=printInfo)
printbtn.grid(row=4, column=1, sticky="w")
insertbtn = Button(root, text="Insert at Cursor", command=insertInfoCursor)
insertbtn.grid(row=4, column=2, sticky="we")
insertbtn = Button(root, text="Insert at End", command=insertInfoEnd)
insertbtn.grid(row=5, column=2, sticky="we")
insertbtn = Button(root, text="Insert at Head", command=insertInfoHead)
insertbtn.grid(row=6, column=2, sticky="we")
# clearbtn = Button(root, text="Clear", command = clearInfo)
# clearbtn.grid(row=4, column= 3, sticky="w")
quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=7, column=2, sticky="we")
root.mainloop()
