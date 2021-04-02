from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.new_speed = STARTING_MOVE_DISTANCE

    def car_gen(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            n_c = Turtle("square")
            n_c.turtlesize(stretch_len=2, stretch_wid=1)
            n_c.penup()
            n_c.color(random.choice(COLORS))
            g = random.randint(-250, 250)
            n_c.goto(x=300, y=g)
            self.all_cars.append(n_c)

    def move(self):
        for car in self.all_cars:
            car.backward(self.new_speed)

    def reset(self):
        self.new_speed += MOVE_INCREMENT
        print(self.new_speed)