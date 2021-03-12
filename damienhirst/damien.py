import colorgram
import random
from turtle import Turtle, Screen, colormode

d = Turtle()
# colors = colorgram.extract('image.jpg', number_of_colors=30)
# print(colors)

rgb = [(244, 242, 243), (29, 31, 48), (151, 183, 206), (188, 69, 45), (239, 241, 244), (60, 36,30),
       (252, 238, 112), (214, 96, 48), (226, 163, 166), (135, 183, 181), (41, 44, 42), (215, 159, 163), (194, 149, 133),
       (224, 171, 167), (49, 33, 36), (81, 86, 80)]
d.penup()
d.setheading(225)
d.forward(300)
d.setheading(0)
d.speed(30)
number_of_dots = 100

for i in range(1, number_of_dots+1):
    colormode(255)
    color_choice = random.choice(rgb)
    d.dot(20, color_choice)
    d.forward(50)
    if i % 10 == 0:
        d.setheading(90)
        d.forward(50)
        d.setheading(180)
        d.forward(500)
        d.setheading(0)
d.ht()
s = Screen()
s.exitonclick()
