"""
client
"""

from service import *


# settings and init
bankService = BankService()


def main():
    # header
    print("=======================")
    print("====My Bank Service====")
    print("======Version 1.0======")
    print("=======================")

    while True:
        print("<<< Main Menu >>>")
        print("[S] Query for interest rate of a single bank")
        print("[A] Query for all interest rates")
        print("[Q] Quit")
        print("Please choose and option: ", end="")
        optionCode = input()

        if optionCode == "q" or "Q":
            print("\nBye!")
            break

        if optionCode == "s" or "S":
            pass


if __name__ == '__main__':
    main()
