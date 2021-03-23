from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, a, b):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=a, y=b)

    def paddle_up(self):
        g = self.ycor() + 20
        self.goto(x=self.xcor(), y=g)

    def paddle_down(self):
        h = self.ycor() - 20
        self.goto(x=self.xcor(), y=h)
