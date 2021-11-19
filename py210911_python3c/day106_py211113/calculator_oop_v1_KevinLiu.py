"""
[Homework]
Date: 2021-11-13
Due date: 2021-11-19
Project: A power calculator in OOP
1. Design a calculator class and implement it in OOP
Requirements:
r1. The calculator should support conversion between numbers and words in English or French
Sample: 127
Expected result:  one hundred and twenty seven
r2. The calculator should support conversion among binary, hexadecimal, decimal
r3. The calculator should support arithmetic operation
r4. The calculator should support logical operation
2. Write a client app and use the calculator class
Requirements:
1. Write your own client app and use it.
2. Use another client app written by other programmers
"""

zero_nine = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

ten_nineteen = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen",
}

twenty_hundred = {
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
}

hundred = "hundred"
thousand = "thousand"
million = "million"


class Entry:
    def __init__(self, user_input):
        self.statement = str(user_input)

    def conver_numbers_words(self):
        global output
        lenght = len(self.statement)

        if lenght == 1:
            output = zero_nine[self.statement]

        if lenght == 2:
            if self.statement[lenght - 2] != "1":
                tens = twenty_hundred[self.statement[lenght - 2] + "0"]
                ones = zero_nine[self.statement[lenght - 1]]
                tens = tens + "-" + ones
            else:
                tens = ten_nineteen[self.statement[-1]]

            output = f"{tens}"

        if lenght == 3:
            hundreds = f"{zero_nine[self.statement[lenght-3]]} {hundred}"
            if self.statement[lenght - 2] != "1":
                tens = twenty_hundred[self.statement[lenght - 2] + "0"]
                ones = zero_nine[self.statement[lenght - 1]]
                tens = tens + "-" + ones
            else:
                tens = ten_nineteen[self.statement[-1]]

            output = f"{hundreds} and {tens}"

        if lenght == 4:
            thousands = f"{zero_nine[self.statement[lenght-4]]} {thousand}"
            hundreds = f"{zero_nine[self.statement[lenght-3]]} {hundred}"
            if self.statement[lenght - 2] != "1":
                tens = twenty_hundred[self.statement[lenght - 2] + "0"]
                ones = zero_nine[self.statement[lenght - 1]]
                tens = tens + "-" + ones
            else:
                tens = ten_nineteen[self.statement[-1]]

            output = f"{thousands} {hundreds} and {tens}"

        if lenght == 5:
            if self.statement[lenght - 5] != "1":
                tens = twenty_hundred[self.statement[lenght - 5] + "0"] + "-" + zero_nine[self.statement[lenght - 4]]
            else:
                tens = ten_nineteen[self.statement[-4]]
            tens_thousands = f"{tens} {thousand}"
            hundreds = f"{zero_nine[self.statement[lenght-3]]} {hundred}"
            if self.statement[lenght - 2] != "1":
                tens = twenty_hundred[self.statement[lenght - 2] + "0"]
                ones = zero_nine[self.statement[lenght - 1]]
                tens = tens + "-" + ones
            else:
                tens = ten_nineteen[self.statement[-1]]

            output = f"{tens_thousands} {hundreds} and {tens}"

        print(output.capitalize())
        print()


# main program
mode = int(input('Please enter a mode. \n"0" for Arithmetic and logical operations, or "1" for number to string conversion.\n'))

if mode == 1:
    while 1:
        print("Mode : Number to string conversion. Maximum is 99 999 (for now).")
        user_input = input("Please enter an integer (no spaces, cannot start with a '0'): ")
        new_calculator_line = Entry(user_input)
        new_calculator_line.conver_numbers_words()
