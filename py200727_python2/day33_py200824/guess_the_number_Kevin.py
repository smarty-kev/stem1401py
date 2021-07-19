"""
Guess the number game
Author : Kevin
Created date : 2020-08-24
Last modified date : 2020-08-24
"""
# generate a number for answer
import random
max = 1001
answer = random.randrange(1, max)

# title
print("===Welcome to Guess the Number!===")

# difficulties
difficulties = ["1. Beginner","2. Intermediate","3. Medium","4. Hard","5. Pro","6. Impossible"]

# number of guesses
num_guesses = [20,10,8,6,3,2]


# print menu
for diff in difficulties:
    print(diff)

# choice of difficulty
diff = int(input("Choose your difficulty: "))


# rules explanation
print(f"The answer is a random number from 1 and {max-1}.")

# limit of guesses
limit = num_guesses[diff-1]

# fail count
fails = 0


# echo number of choices you have
def echoguesscount():
    print("You have {} guesses.".format(num_guesses[diff-1]-fails))


# initial amount of guesses
echoguesscount()


# check if guess if correct
def checkanswer(guess, answer):
    if guess > answer:
        print("Your guess is too big.")  # comparison
        print("You have {} remaining guess.".format(limit - fails))  # echo remaining guess
    elif guess < answer:
        print("Your guess is too small.")  # comparison
        print("You have {} remaining guess.".format(limit - fails))  # echo remaining guess


# user guess
def askinput():
    guess = int(input("Your guess? "))
    return guess


guess = 0

# while loop
while guess != answer:
    guess = askinput()
    fails += 1
    checkanswer(guess, answer)
    if fails == limit:
        print("Game Over!")
        print("The answer was {}.".format(answer))
        break
else:
    print("Bingo")
