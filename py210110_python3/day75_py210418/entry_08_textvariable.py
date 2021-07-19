"""
textvariable
change value of Entry by set()
reference: https://blog.csdn.net/weixin_42272768/article/details/100592533
"""
from tkinter import *


def set_entry():
    content1 = txt.get()
    print("text at original entry = ", content1)
    txt2.set(content1)


root = Tk()
root.title("Python GUI - Entry")
# root.geometry("360x160")
txt = StringVar()
txt2 = StringVar()
label1 = Label(root, text="Origin").grid(row=1, column=1, padx=(50, 0))
b1 = Entry(root, textvariable=txt, width=30)
b1.grid(row=1, column=2, padx=(0, 50))
label2 = Label(root, text="Target").grid(row=2, column=1, padx=(50, 0))
b2 = Entry(root, textvariable=txt2, width=30)
b2.grid(row=2, column=2, padx=(0, 50))
b3 = Button(root, text='Copy Text', command=set_entry)
b3.grid(row=3, column=2, sticky="we", padx=(0, 50))
root.mainloop()
