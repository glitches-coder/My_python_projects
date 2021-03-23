from turtle import Turtle, Screen, colormode
import random
t = Turtle()
t.speed("fastest")
t.pensize(2)
s = Screen()
s.bgcolor('black')
def spiro():
    counter = 0

    while counter != 100:
        colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        my_tup = (r, g, b)
        t.pencolor(my_tup)
        t.circle(100)
        t.tilt(10)
        t.left(10)
        counter += 1


spiro()


s.exitonclick()
