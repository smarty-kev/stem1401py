"""
Entry
delete or clear content from an entry
"""
from tkinter import *
def printInfo():
    print(f"You've input: {entry1.get()}")
def insertInfo():
    entry1.insert(2,"-insert-")
    print(f"You've input: {entry1.get()}")
def insertInfoLambda(pos=END):
    print(f"You've input: {entry1.get()}")
    return lambda: entry1.insert(pos,"-insert-")
def clearInfoAll():
    entry1.delete(0, END)
root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")
accountL = Label(root, text="Input ")
accountL.grid(row=2,padx=(50,5), sticky='e')
entry1 = Entry(root)
entry1.grid(row=2, column=1, padx=(5, 50), columnspan=3)
printbtn = Button(root, text="Print", command = printInfo)
printbtn.grid(row=4, column= 1, sticky="w")
insertbtn = Button(root, text="Insert normal", command=insertInfo)
insertbtn.grid(row=4, column= 2, sticky="w")
insertbtn = Button(root, text="Insert lambda", command=insertInfoLambda())
insertbtn.grid(row=4, column= 3, sticky="w")
clearbtn = Button(root, text="Clear All", command=clearInfoAll)
clearbtn.grid(row=5, column= 2, sticky="we")
quitbtn = Button(root, text="Quit", command=root.destroy)
quitbtn.grid(row=5, column= 3, sticky="we")
root.mainloop()