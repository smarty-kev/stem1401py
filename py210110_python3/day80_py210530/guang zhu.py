"""
[Exam]
30/05/2021
Guang Zhu Cui


Writing a GUI program in Python tkinter for the registration process of a network application.

Basic requirements:
a. User can input a username

b. User can input a password

c. User can input a password for the second time to ensure user's password was input correctly

d. User can input a validation code (usually an integer) generated randomly by the System,
and that code (or number) should display on the window.

If the user inputs the wrong code (or number), registration will fail and a messagebox should popup on the screen to warn the user.
e. A text title for this application should be set properly on the interface. Note: It is not the title of the main window.

f. A Button is required to perform registration once User finishes all inputs.
Proper messages or information is required to display in both cases of 'success' and 'failed'.

g. A second Button is required to perform reset (or clear all inputs on the window)

h. Another Button is required to perform closing window and exit
"""

from tkinter import *
from tkinter import messagebox as msg
import random

root = Tk()
root.title("User register form")
root.geometry()

validation_code_confirmed = 0


def Register():
    global validation_code_confirmed
    title_login_succeed = 'Registered'
    login_succeed = 'Succeed!! Now you can login at any time!'
    title_login_failed = 'Login failed'
    login_failed = 'Login failed. Please enter the same password at the confirmation or confirm the validation code.'
    password = passwordE.get()
    confirm_password = Confirm_passwordE.get()
    if password == confirm_password and validation_code_confirmed == 1:
        msg.showinfo(title_login_succeed, login_succeed)
    else:
        msg.showerror(title_login_failed, login_failed)


def validation_msgbox():
    global validation_code_confirmed
    title_wrong = 'Wrong code'
    text_wrong = 'Please enter the correct code'
    title_correct = 'Correct code!'
    text_correct = 'Succeed!! Please continue your registeration now!'
    validation_code_user_entered = Validation_code_entry.get()
    if validation_code_user_entered != code:
        msg.showerror(title_wrong, text_wrong)
    else:
        msg.showinfo(title_correct, text_correct)
        validation_code_confirmed = 1


def Reset():
    accountE.delete(0, END)
    passwordE.delete(0, END)
    Confirm_passwordE.delete(0, END)
    Validation_code_entry.delete(0, END)


title = Label(root, text='Register your account!', font='Times 36 bold')
title.grid(row=1, columnspan=4)

accountL = Label(root, text="Username: ")
accountL.grid(row=2, padx=(50, 5), sticky='e')
accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))

passwordL = Label(root, text='Password:')
passwordL.grid(row=3, padx=(50, 5), sticky='e')
passwordE = Entry(root)
passwordE.grid(row=3, column=1, padx=(5, 50))

Confirm_passwordL = Label(root, text='Confirm password:')
Confirm_passwordL.grid(row=4, padx=(50, 5), sticky='e')
Confirm_passwordE = Entry(root)
Confirm_passwordE.grid(row=4, column=1, padx=(5, 50))

Validation_code_entry_label = Label(root, text='Please enter the code:')
Validation_code_entry_label.grid(row=5, padx=(50, 5), sticky='e')
Validation_code_entry = Entry(root)
Validation_code_entry.grid(row=5, column=1, padx=(5, 50))

code = str(random.randint(1, 99))

if len(code) < 2:
    code = '0' + code
Validation_code = Label(root, text=f'code:{code}')
Validation_code.grid(row=5, column=2)
Validation_code_btn = Button(root, text='confirm code', command=validation_msgbox)
Validation_code_btn.grid(row=5, column=3)

loginbtn = Button(root, text="Register", command=Register)
loginbtn.grid(row=6, column=0, sticky="e")

resetbtn = Button(root, text='Reset', command=Reset)
resetbtn.grid(row=6, column=1)

exitbtn = Button(root, text="Exit", command=root.destroy)
exitbtn.grid(row=6, column=2, sticky="w")

root.mainloop()
