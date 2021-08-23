"""

"""


from tkinter import *
from tkinter.ttk import Separator


root = Tk()
root.title("Text")
root.geometry("640x480+200+200")
root.config(bg="light gray")

text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

text.insert(END, "Write text here")

# separator
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# status bar
var = StringVar()
var.set("Status : Insert Mode")
status_bar = Label(root, textvariable=var, bg="light gray")
status_bar.pack(anchor=S+W)


root.mainloop()
