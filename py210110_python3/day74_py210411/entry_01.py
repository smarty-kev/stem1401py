"""

"""

from tkinter import *

root = Tk()
root.title("Kevin L")
root.geometry("350x205+200+200")
root.config(bg="#ddddff")


accountL = Label(root, text="Account")
accountL.grid(row=2, padx=(50,5), sticky="e")

passwordL = Label(root, text="Password")
passwordL.grid(row=3, padx=(50,5), sticky="e")

accountE = Entry(root, width=20)
accountE.grid(row=2, column=1, padx=(5, 50), sticky="e")

passwordE = Entry(root, show="*", width=20)
passwordE.grid(row=3, column=1, padx=(5, 50), sticky="e")

root.mainloop()
