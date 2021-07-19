"""
infinite loop
"""

# while True:
#     print("while loop never stops")

# while 1:
#     print("while loop never stops")

# while "not empty string":
#     print("while loop never stops")

while "not empty string":
    # print("while loop never stops")
    # if user input the command of 'exit'
    # the terminate infinite loop
    cmd = input("Enter a command: ")
    if cmd == "exit":
        break
    print(cmd)
