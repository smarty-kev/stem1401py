"""
Web Registration
Author : Kevin Liu
Date of last modification : 30 May 2021
This was written on MacOs Sierra Version 10.12.6 (16G2136)
"""

# import different modules
from tkinter import *
import random
from tkinter import messagebox


# def functions
def confirm():
    password = password_E.get()
    confirmation_password = password_confirmation_E.get()
    user_captcha = user_captcha_E.get()
    username = username_E.get()

    if password == confirmation_password and user_captcha == code:
        messagebox.showinfo("Success", f"You have created you account, we look forward to working with you in the future {username}!")
    else:
        messagebox.showerror("Error", "There was an error during the creation of your account, please try again!")


def reset():
    username_E.delete(0, END)
    password_E.delete(0, END)
    password_confirmation_E.delete(0, END)
    user_captcha_E.delete(0, END)


def close_window():
    root.destroy()


# main window specs
root = Tk()
root.title("Web Registration | Kevin L.")
root.geometry("+200+200")


# title label
title_L = Label(text="Create you account here!", font=(None, 30))
title_L.grid(columnspan=3)


# main program

# username - label and entry
username_L = Label(text="Username :")
username_L.grid(column=0)

username_E = Entry()
username_E.grid(row=1, column=1, columnspan=2)


# password - label and entry
password_L = Label(text="Password :")
password_L.grid(column=0)

password_E = Entry()
password_E.grid(row=2, column=1, columnspan=2)


# password confirmation - label and entry
password_confirmation_L = Label(text="Confirm password :")
password_confirmation_L.grid(column=0)

password_confirmation_E = Entry()
password_confirmation_E.grid(row=3, column=1, columnspan=2)


# captcha (validation code)
instruction_L = Label(text="Please solve the following captcha:")
instruction_L.grid(columnspan=3)

user_captcha_E = Entry(width=10)
user_captcha_E.grid(column=0)

instruction_2_L = Label(text="Your captcha:")
instruction_2_L.grid(row=5, column=1)

code = ""
for digit in range(5): # 5 = length of code
    code += str(random.randint(0, 9))
captcha = Label(text=code)
captcha.grid(row=5, column=2)

# create account button
confirm_B = Button(text="Confirm", height=2, command=confirm)
confirm_B.grid(column=0, pady=10)

# reset button
reset_B = Button(text="Reset", height=2, command=reset)
reset_B.grid(column=1, row=6)

# close button
close_window_B = Button(text="Exit", height=2, command=close_window)
close_window_B.grid(column=2, row=6)

root.mainloop()
