"""
[Challenge]  Project. Volume Controller
c04_button/button_03_b.py
Description
Max value and Min value
1. User can press '+' button to increase the number by one per click
2. User can press '-' button to decrease the number by one per click
3. The number shows in a Label
constraints:
the MAX value = 10,
the MIN value = -10,
default number = 0
default step number = 1,  step number is adjustable
"""

# tkinter module
from tkinter import *

# digit (start = 0)
digit = 0

# step number
step_number = 1

MAX = 10
MIN = -10


# add 2
def add():
    global digit
    if digit == MIN:
        sub_button.config(state="normal")
    digit += step_number
    digit_label.config(text=digit)
    if digit == MAX:
        add_button.config(state="disabled")


# sub 2
def sub():
    global digit
    if digit == MAX:
        add_button.config(state="normal")
    digit -= step_number
    digit_label.config(text=digit)
    if digit == MIN:
        sub_button.config(state="disabled")


# widget specifications
root = Tk()
root.title("Kevin L. | Volume Controller")
root.geometry("350x205+200+200")
root.config(bg="#ddddff")
root.resizable(0, 0)


# label with digit
digit_label = Label(text=digit, font="Helvetica 25", width=45, height=5, bg="gray85")
digit_label.pack()

# exit button
exit_button = Button(width=14, height=5, text="Exit", relief="raised", command=root.destroy)
exit_button.pack(padx=16, pady=11, anchor=S, side=RIGHT)

# + button
add_button = Button(width=8, height=5, text="+", relief="raised", command=add)
add_button.pack(pady=11, anchor=S, side=RIGHT)

# - button
sub_button = Button(width=8, height=5, text="-", relief="raised", command=sub)
sub_button.pack(padx=19, pady=11, anchor=S, side=RIGHT)

# mainloop
root.mainloop()
