"""

"""

from tkinter import *
from tkinter import messagebox as msg


def helloCallBack():
    title = "Show Message"
    text = "Hello Python Tkinter"
    # msg.showinfo(title, text)
    msg.showerror(title, text)

# widget specifications
root = Tk()
root.title("Kevin L. Homework")
root.geometry("800x450+200+200")
root.config(bg="gray85")


# btn 1
show_message_btn = Button(root, text="Show Message", command=helloCallBack)
show_message_btn.pack()

# btn 2
close_btn = Button(root, text="Close", command=root.destroy)
close_btn.pack()

# mainloop
root.mainloop()
