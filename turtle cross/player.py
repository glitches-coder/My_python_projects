from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=y)

    def player_reset(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
