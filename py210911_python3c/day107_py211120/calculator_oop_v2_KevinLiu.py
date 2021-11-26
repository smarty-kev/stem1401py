"""
[Homework]
Date: 2021-11-20
Due date: 2021-11-27
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

categories = {0: "", 3: "thousand ", 6: "million ", 9: "billion ", 12: "trillion ", 15: "quadrillion ", 18: "quintillion ", 21: "sextillion ", 24: "septillion ", 27: "octillion ", 30: "nonillion "}
one_nine = ["", "one ", "two ", "three ", 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
ten_ninety = {0: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
teens = {11: "eleven ", 12: "twelve ", 13: "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ", 17: "seventeen ", 18: "eighteen ", 19: "nineteen "}


class Calculator:
    def __init__(self, user_entry, logical_mode=None):
        self.statement = user_entry
        self.logical_mode = logical_mode

    def convert_numbers_words(self):
        exit = False
        next_num = ""
        next_word = ""
        output = ""
        input_str = self.statement
        if input_str == 'change mode':
            exit = True

        if exit == False:
            if input_str == "0":
                return "zero"
            for i in range(len(input_str)):
                if i % 3 == 0:
                    if i == len(input_str)-1:
                        output = one_nine[int(input_str[-i - 1])] + categories[i] + output
                        next_word = one_nine[int(input_str[-i - 1])]
                        next_num = input_str[-i - 1]
                    else:
                        if input_str[-i-1] != "0" or input_str[-i-2] != "0" or input_str[-i-3] != "0":
                            output = categories[i] + output
                            next_word = one_nine[int(input_str[-i - 1])]
                            next_num = input_str[-i - 1]

                elif i % 3 == 1:
                    if input_str[-i-1] == "1":
                        if next_word != "":
                            output = teens[int(input_str[-i-1] + next_num)] + output
                            next_word = teens[int(input_str[-i-1] + next_num)]
                        else:
                            output = "ten " + output
                    elif input_str[-i-1] == "0":
                        output = one_nine[int(input_str[-i])] + output
                        next_word = ""
                    else:
                        if input_str[-i] != "0":
                            output = ten_ninety[int(input_str[-i-1])] + "-" + one_nine[int(input_str[-i])] + output
                            next_word = ten_ninety[int(input_str[-i-1])]
                        else:
                            output = ten_ninety[int(input_str[-i-1])] + " " + output
                            next_word = ten_ninety[int(input_str[-i-1])]
                else:
                    if input_str[-i-1] != "0":
                        if next_word == "" and input_str[-i+1] == "0":
                            output = one_nine[int(input_str[-i-1])] + "hundred " + output
                        else:
                            output = one_nine[int(input_str[-i-1])] + "hundred and " + output
        output = output.capitalize()
        return output

    def arithmetic(self):
        answer = eval(self.statement)
        return answer

    def logical_true_false(self):
        if self.statement[0] == "True":
            self.statement[0] = True
        if self.statement[0] == "False":
            self.statement[0] = False
        if self.statement[1] == "True":
            self.statement[1] = True
        if self.statement[1] == "False":
            self.statement[1] = False

    def logical_and(self):
        self.logical_true_false()
        return self.statement[0] and self.statement[1]

    def logical_or(self):
        self.logical_true_false()
        return self.statement[0] or self.statement[1]

    def logical_not(self):
        self.logical_true_false()
        return not self.statement

    def execute_arithmetic_logical_operation(self, sub_mode):
        if sub_mode == '0':
            return self.arithmetic()

        if sub_mode == '1':
            if self.logical_mode == '0':
                self.logical_and()
            if self.logical_mode == '1':
                self.logical_or()
            if self.logical_mode == '2':
                self.logical_not()


# main program
mode = int(input('Please enter a mode. \n"0" for Arithmetic and logical operations,'
                 ' or "1" for number to string conversion.\n'))
modes = ["Arithmetic and logical operations", "Number to string conversion"]
while 1:
    print(f"Mode : {modes[mode]}. To change mode, type 'change mode'.")

    if mode == 1:
        user_input = input("Please enter an integer (no spaces, cannot start with a '0'): ")
        new_calculator_line = Calculator(user_input)
        print(new_calculator_line.convert_numbers_words())
        print()
    if mode == 0:
        logical_mode = None
        sub_mode = input("'0' for arithmetic, '1' for logical. ")
        if sub_mode == '0':
            user_input = input("Please enter a mathematical operation: ")
        if sub_mode == '1':
            logical_mode = input("'0' for logical_and, '1' for logical_or, '2' for logical_not. ")
            if logical_mode == '0' or '1':
                x = input("Please enter the first variable: ")
                y = input("Please enter the second variable: ")
                user_input = [x, y]
            if logical_mode == '2':
                user_input = input("Please enter the variable: ")

        new_calculator_line = Calculator(user_input, logical_mode)
        print(new_calculator_line.execute_arithmetic_logical_operation(sub_mode))

    if user_input == 'change mode':
        if mode == 0:
            mode = 1
        else:
            mode = 0