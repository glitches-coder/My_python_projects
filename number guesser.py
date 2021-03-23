# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art2 import logo

print(logo)


def guess(x):
    i = 0
    for i in range(0, x):
        compare(x-i)

    if i == x:
        print(f"You lose. the number was {number}")


def compare(y):
    print(f"You have {y} turns left")
    user_ch = int(input("Enter a number: "))

    if number == user_ch:
        print("You win")
        exit()
    elif user_ch > number:
        print("Too high")
    else:
        print("Too low")


number = random.choice(list(range(1, 101)))

level = input("Which difficulty do you want to play in ? easy, medium, hard: ")
level = level.lower()
if level == "easy":
    guess(10)
elif level == "medium":
    guess(5)
elif level == "hard":
    guess(3)


