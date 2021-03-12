# - link logos and stuff
# - find a way to fetch keys from dictionary and link them in one statement
# - insert vs symbol in between both the statement
# - create a compare function to compare and check answer
# - create a link which will send compare B to compare A and replace compare B
# - add the score to variable which adds up in every correct answer
# - finally if user answers wrong end game and display final score

from art3 import logo

print(logo)
from art3 import vs
from game_data import data
import random
import os


def shuffler():
    return random.choice(data)


def initializer(account):
    nm = account["name"]
    desc = account["description"]
    ctry = account["country"]
    return f"{nm}, {desc} from {ctry}"


def combine(user_ans, acc_1, acc_2):
    if acc_1 > acc_2:
        return user_ans == "a"
    else:
        return user_ans == "b"


def game():
    adder = 0
    game_cont = True
    user_acc_2 = shuffler()

    while game_cont:
        user_acc_1 = user_acc_2
        user_acc_2 = shuffler()
        while user_acc_1 == user_acc_2:
            user_acc_2 = shuffler()

        print(f"Compare A: {initializer(user_acc_1)}.")
        print(vs)
        print(f"Compare B: {initializer(user_acc_2)}.")
        user_ans = input("Choose 'A' or 'B': \n").lower()
        acc_1 = user_acc_1["follower_count"]
        acc_2 = user_acc_2["follower_count"]
        is_correct = combine(user_ans, acc_1, acc_2)

        os.system("cls")

        if is_correct:
            adder += 1
            print(f"Your score is {adder}")
        else:
            game_cont = False
            print(f"sorry that was the wrong answer. Your score is {adder}")


game()
