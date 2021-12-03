"""
[Homework]
Date: 2021-11-27
Due date: 2021-12-03
Project: A power calculator in OOP
Continue to design and implement
Hints:
Polish R1
Coding for R2, R3
"""


class Calculator:
    categories = {0: "", 3: "thousand ", 6: "million ", 9: "billion ", 12: "trillion ", 15: "quadrillion ",18: "quintillion ", 21: "sextillion ", 24: "septillion ", 27: "octillion ", 30: "nonillion "}
    one_nine = ["", "one ", "two ", "three ", 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
    ten_ninety = {0: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    teens = {11: "eleven ", 12: "twelve ", 13: "thirteen ", 14: "fourteen ", 15: "fifteen ", 16: "sixteen ", 17: "seventeen ", 18: "eighteen ", 19: "nineteen "}

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
                        output = self.one_nine[int(input_str[-i - 1])] + self.categories[i] + output
                        next_word = self.one_nine[int(input_str[-i - 1])]
                        next_num = input_str[-i - 1]
                    else:
                        if input_str[-i-1] != "0" or input_str[-i-2] != "0" or input_str[-i-3] != "0":
                            output = self.categories[i] + output
                            next_word = self.one_nine[int(input_str[-i - 1])]
                            next_num = input_str[-i - 1]

                elif i % 3 == 1:
                    if input_str[-i-1] == "1":
                        if next_word != "":
                            output = self.teens[int(input_str[-i-1] + next_num)] + output
                            next_word = self.teens[int(input_str[-i-1] + next_num)]
                        else:
                            output = "ten " + output
                    elif input_str[-i-1] == "0":
                        output = self.one_nine[int(input_str[-i])] + output
                        next_word = ""
                    else:
                        if input_str[-i] != "0":
                            output = self.ten_ninety[int(input_str[-i-1])] + "-" + self.one_nine[int(input_str[-i])] + output
                            next_word = self.ten_ninety[int(input_str[-i-1])]
                        else:
                            output = self.ten_ninety[int(input_str[-i-1])] + " " + output
                            next_word = self.ten_ninety[int(input_str[-i-1])]
                else:
                    if input_str[-i-1] != "0":
                        if next_word == "" and input_str[-i+1] == "0":
                            output = self.one_nine[int(input_str[-i-1])] + "hundred " + output
                        else:
                            output = self.one_nine[int(input_str[-i-1])] + "hundred and " + output
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

    def convert_hex_to_decimal(self):
        hex_data = self.statement
        dec_data = int(hex_data, 16)
        return dec_data

    def convert_hex_to_binary(self):
        hex_data = self.statement
        bin_data = bin(int(hex_data, 16))
        return bin_data

    def convert_binary_to_hex(self):
        bin_data = self.statement
        hex_data = hex(int(bin_data, 2))
        return hex_data

    def convert_binary_to_decimal(self):
        bin_data = self.statement
        dec_data = int(bin_data, 2)
        return dec_data

    def convert_decimal_to_hex(self):
        dec_data = int(self.statement)
        hex_data = hex(dec_data)
        return hex_data

    def convert_decimal_to_binary(self):
        dec_data = int(self.statement)
        bin_data = bin(dec_data)
        return bin_data


# main program
mode = int(input('Please enter a mode. \n"0" for Arithmetic and logical operations,'
                 ' or "1" for number to string conversion or "2" for conversions bewteen hex, dec, binary.\n'))
modes = ["Arithmetic and logical operations", "Number to string conversion", "Conversion between hex, dec, binary"]
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

    if mode == 2:
        original_data_form = input("Please enter the original data form (hex, decimal or binary) :")
        new_data_form = input("Please enter the new data form :")
        user_input = input("The number (ex: 8, OF, 10101010) :")
        new_calculator_line = Calculator(user_input)
        if original_data_form == "hex":
            if new_data_form == "decimal":
                print(new_calculator_line.convert_hex_to_decimal())
            if new_data_form == "binary":
                print(new_calculator_line.convert_hex_to_binary())

        if original_data_form == "decimal":
            if new_data_form == "hex":
                print(new_calculator_line.convert_decimal_to_hex())
            if new_data_form == "binary":
                print(new_calculator_line.convert_decimal_to_binary())

        if original_data_form == "binary":
            if new_data_form == "hex":
                print(new_calculator_line.convert_binary_to_hex())
            if new_data_form == "decimal":
                print(new_calculator_line.convert_binary_to_decimal())

    if user_input == 'change mode':
        mode += 1
        if mode == 3:
            mode = 0
