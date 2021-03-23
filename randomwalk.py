from turtle import Turtle, Screen, colormode
import random


def travel():
    d = Turtle()
    d.ht()
    d.pensize(10)
    d.speed(10)

    counter = 0

    while counter != usr:
        colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        my_tup = (r, g, b)
        # color = random.choice(
        #     ["green", "blue", "red", "orange", "lightblue", "aquamarine", "teal", "yellow", "grey", "pink", "magenta",
        #      "lime"])
        x = random.choice([1, 2, 3, 4])
        angle = random.choice([0, 90, 180, 270, 360])
        if x == 1:
            d.forward(25)
            d.left(angle)
            d.pencolor(my_tup)
            counter += 1
        elif x == 2:
            d.forward(25)
            d.left(angle)
            d.pencolor(my_tup)
            counter += 1
        elif x == 3:
            d.forward(25)
            d.left(angle)
            d.pencolor(my_tup)
            counter += 1
        elif x == 4:
            d.forward(25)
            d.left(angle)
            d.pencolor(my_tup)
            counter += 1


usr = int(input("How many steps do you want the program to run? (integer only) : "))

travel()

s = Screen()
s.exitonclick()
