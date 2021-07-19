"""
[Homework]
Date: 2021-03-28
Input N numbers from your keyboard
Put them into a list  (i.e. [1,3,5])
Create a window
Then place(add) N buttons to the window
anchor=S
side=LEFT, side=RIGHT
Button text is the current number you get
Create an 'Exit' button
which allows you to press it to close the window
Hint:
Lambda
pass parameter
only one callback function
Due date: by the end of next Sat.
"""

# tkinter module
from tkinter import *


# print number
def print_number(number):
    print(numbers[number])


# widget specifications
root = Tk()
root.title("Kevin L. Homework")
root.geometry("800x450+200+200")
root.config(bg="gray85")


# number list
numbers = []

# ask user to input N numbers
num = int(input("Please enter a number, a button with the number will be created. When clicked, the number will be echoed on console: "))
print("If you do not wish to add more numbers, type: done")
numbers.append(num)
while True:
    num = input('Please enter a number, or "done" if you are finished: ')
    if num == "done":
        break
    numbers.append(int(num))
# print(numbers)


Button(text="Exit", command=root.destroy).pack(pady=20, padx=15, anchor=S, side=RIGHT)
for i in range(len(numbers)):
    Button(text=numbers[i], command=lambda num=i: print_number(num)).pack(pady=20, padx=15, anchor=S, side=RIGHT)


# mainloop
root.mainloop()
