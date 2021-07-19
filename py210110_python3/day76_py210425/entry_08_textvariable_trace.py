"""
textvariable
trace()
"""
from tkinter import *
def callbackW(*args):
    txt2.set(txt.get())
def callbackR(*args):
    print("Waring: Data is being read!")
def read():
    print("Data read:", txt.get())
    print()
root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")
# entry
txt = StringVar()
entry = Entry(root, textvariable=txt)
entry.pack(padx=20, pady=5)
txt.trace('w', callbackW)
txt.trace('r', callbackR)
# label
txt2 = StringVar()
label = Label(root, textvariable=txt2)
txt2.set("Real-time data shows here")
label.pack(padx=20, pady=5)
# button
btn = Button(root, text="Start to Read", command=read)
btn.pack(padx=20, pady=5)
root.mainloop()