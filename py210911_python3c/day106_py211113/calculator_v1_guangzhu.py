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
number_to_words_ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                        9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
number_to_words_tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
number_to_words_hundreds = ['Hundred']


class calculator():

    def __init__(self, number):
        self.number = number

    def number_to_word(self):
        if 1 <= self.number < 20:
            print(number_to_words_ones[self.number])
        if 20 <= self.number < 100:
            print(number_to_words_tens[int(str(self.number)[0]) - 1] + ' ' + number_to_words_ones[
                int(str(self.number)[1])])
        if 100 <= self.number < 1000 and int(str(self.number)[1] + str(self.number)[2]) < 20:
            print(
                number_to_words_ones[int(str(self.number)[0])] + ' ' + number_to_words_hundreds[0] + ' ' + 'and' + ' ' +
                number_to_words_ones[
                    int(str(self.number)[1] + str(self.number)[2])])
        if 100 <= self.number < 1000 and int(str(self.number)[1] + str(self.number)[2]) > 20:
            print(
                number_to_words_ones[int(str(self.number)[0])] + ' ' + number_to_words_hundreds[0] + ' ' + 'and' + ' ' +
                number_to_words_tens[
                    int(str(self.number)[1]) - 1] + ' ' + number_to_words_ones[int(str(self.number)[2])])


num = eval(input('Please enter a number between 1 to 999:'))
process = calculator(num)
process.number_to_word()