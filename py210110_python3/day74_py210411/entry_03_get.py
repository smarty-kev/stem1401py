"""
Entry
padx(left, right)
get()
"""
from tkinter import *
from tkinter.ttk import Separator
def printInfo():
    print(f"You've input: {accountE.get()}")
root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")
accountL = Label(root, text="Input ")
accountL.grid(row=2,padx=(50,5), sticky='e')
accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))
loginbtn = Button(root, text= "Get text", command = printInfo)
loginbtn.grid(row=4, column= 0, sticky="e")
quitbtn = Button(root, text= "Quit", command = root.destroy)
quitbtn.grid(row=4, column= 1, sticky="w")
root.mainloop()