

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


