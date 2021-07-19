"""
Entry
insert by index of position
"""
from tkinter import *
def printInfo():
    print(f"You've input: {entry1.get()}")
def insertInfo():
    """
    hard code the index (position for insertion)
    :return:
    """
    pos=1
    entry1.insert(pos,"-INSERT-")
    print(f"You've input: {entry1.get()}")
# def clearInfo():
#     entry1.delete(0, END)
root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")
accountL = Label(root, text="Input ")
accountL.grid(row=2,padx=(50,5), sticky='e')
entry1 = Entry(root)
entry1.grid(row=2, column=1, padx=(5, 50), columnspan=3)
printbtn = Button(root, text="Print", command = printInfo)
printbtn.grid(row=4, column= 1, sticky="we")
insertbtn = Button(root, text="Insert normal", command=insertInfo)
insertbtn.grid(row=4, column= 2, sticky="we")
# clearbtn = Button(root, text="Clear", command=clearInfo)
# clearbtn.grid(row=5, column= 2, sticky="we")
quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=5, column= 2, sticky="we")
root.mainloop()