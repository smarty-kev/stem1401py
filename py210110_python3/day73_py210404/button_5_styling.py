"""
Tkinter
create a button
pack layout
styling button
size: padx, pady
color: fg and bg
"""
from tkinter import *
root = Tk()
root.geometry("320x240+200+200")
root.config(bg="#ddddff")
root.title("Python GUI - Button Style")
btn1 = Button(root, text='Confirm')
btn1.pack(padx=50)
btn2 = Button(root, text='Click', padx=50, pady=10)
btn2.pack(padx=50)
btn3 = Button(root, text='Click', padx=50, pady=10, fg="white",bg="blue")
btn3.pack(padx=50)
btn3 = Button(root, text='Click', padx=50, pady=10, fg="white",bg="#ff0000")
btn3.pack(padx=50)
root.mainloop()