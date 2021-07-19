"""
6 difficulties
"""

"""
plan.
choose the difficulty
generate a random number from 1-100
depending on the difficulty, they have a certain amount of guesses
user can input their guess, if correct -> finish
if incorrect, echos if the guess is too high or too low
"""


# title of the game
print("===Welcome to Guess the Number!===")

# difficulties
print("Please select your difficulty: ")
difficulties = ["1. Beginner","2. Intermediate","3. Medium","4. Hard","5. Pro","6. Impossible"]

# number of guesses
num_guesses = [18,12,10,7,5,2]

# print
for diff in difficulties:
    print(diff)

# user chooses the difficulty
difficulty = int(input("Please enter the corresponding number: "))

# generate the random number
import random
answer = random.randint(1,101)


# function
def user_inp_guess():
    guess = int(input("Your guess?  "))


# rules explanation
print("The answer is a number from 1 and 100.")

guess = 0

# error count
error_count = 0

# if user guess is false
while guess != answer:
    error_count += 1
    if error_count == num_guesses[difficulty-1]:
        print("You have used up all your guesses.")
        print("Game over! :(")
        print("The answer was {}".format(answer))
        break
    if guess > answer:
        print("Your answer is too big.")
    elif guess < answer:
        print("Your answer is too small.")
    print("You have {} remaining guesses.".format(num_guesses[difficulty-1] - error_count))
    guess = int(input("Your guess?  "))
else:
    print("Congratulations! You win! :)")
