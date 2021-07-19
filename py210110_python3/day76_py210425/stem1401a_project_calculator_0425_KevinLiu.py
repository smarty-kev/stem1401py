"""
Create a window
Create 10 Button objects for digit 0 - 9
Create 7 Button objects for operators (+, -, *, /, %, ., =)
where % stands for modulus operator rather than percentage sign
where = stands for performing calculation
Create a "Clear all" Button with the caption of C
Create a "Backspace" Button with the caption of DEL
Create a display Label to show expression (or equation) at the first line
and to show result at the second line.
"""

# tkinter module
from tkinter import *


# def functions
def user_input_digit(num):
    new_expression = t_var.get() + str(num)
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def clear_all():
    t_var.set("")
    display_Label.config(textvariable=t_var)


def delete():
    expression = t_var.get()
    t_var.set(expression[:-1])
    display_Label.config(textvariable=t_var)


def modulus():
    new_expression = t_var.get() + "%"
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def division():
    new_expression = t_var.get() + "/"
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def multiplication():
    new_expression = t_var.get() + "*"
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def subtraction():
    new_expression = t_var.get() + "-"
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def addition():
    new_expression = t_var.get() + "+"
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def comma():
    new_expression = t_var.get() + ","
    t_var.set(new_expression)
    display_Label.config(textvariable=t_var)


def equal():
    try:
        answer = eval(t_var.get())
        expression_answer = t_var.get()+"\n"+str(answer)
        t_var.set(expression_answer)
        display_Label.config(textvariable=t_var)
    except Exception:
        t_var.set("Error")
        display_Label.config(textvariable=t_var)


# font
font = ("Helvetica", 16)

# widget specifications
root = Tk()
root.title("Python")
root.geometry("600x350+200+200")
root.config(bg="gray85")
root.resizable(1, 1)


# display Label
t_var = StringVar()
display_Label = Label(textvariable=t_var, width=63, height=3, bg="gray85", relief="raised", padx=5, anchor=E, font=font)
display_Label.grid(columnspan=4, padx=10, pady=10, sticky=E)

# button 0 - 9 (creation)
digit_button_list = []
n_digit_button = 10  # number of digit buttons (0-9)
for i in range(n_digit_button):
    button = Button(text=i, command=lambda num=i: user_input_digit(num), width=15, height=2, font=font)
    digit_button_list.append(button)

# all special buttons
clear_all_B = Button(text="C", font=font, fg="blue", width=15, height=2, command=clear_all)
clear_all_B.grid(column=0, padx=(5, 0))

delete_B = Button(text="DEL", font=font, width=15, height=2, command=delete)
delete_B.grid(row=1, column=1)

modulus_B = Button(text="%", font=font, width=15, height=2, command=modulus)
modulus_B.grid(row=1, column=2)

division_B = Button(text="/", font=font, width=15, height=2, command=division)
division_B.grid(row=1, column=3, padx=(0, 5))

multiplication_B = Button(text="*", font=font, width=15, height=2, command=multiplication)
multiplication_B.grid(row=2, column=3)

subtraction_B = Button(text="-", font=font, width=15, height=2, command=subtraction)
subtraction_B.grid(row=3, column=3)

addition_B = Button(text="+", font=font, width=15, height=2, command=addition)
addition_B.grid(row=4, column=3)

comma_B = Button(text=".", font=font, width=15, height=2, command=comma)
comma_B.grid(row=5, column=2)

equal_B = Button(text="=", font=font, width=15, height=2, command=equal)
equal_B.grid(row=5, column=3)


# grid button 0 - 9
digit_button_list[0].config(width=30)
digit_button_list[0].grid(row=5, columnspan=2, pady=5, padx=(5, 0), sticky="we")
digit_button_list[7].grid(row=2, column=0, pady=5, padx=5)
digit_button_list[8].grid(row=2, column=1, pady=5, padx=5)
digit_button_list[9].grid(row=2, column=2, pady=5, padx=5)
digit_button_list[4].grid(row=3, column=0, pady=5, padx=5)
digit_button_list[5].grid(row=3, column=1, pady=5, padx=5)
digit_button_list[6].grid(row=3, column=2, pady=5, padx=5)
digit_button_list[1].grid(row=4, column=0, pady=5, padx=5)
digit_button_list[2].grid(row=4, column=1, pady=5, padx=5)
digit_button_list[3].grid(row=4, column=2, pady=5, padx=5)


# mainloop
root.mainloop()
