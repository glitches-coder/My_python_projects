from turtle import Turtle

FONT = ("OpenSans", 11, "bold")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.updater()

    def updater(self):
        self.write(f"Your score is = {self.score}", align=ALIGN, move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGN, move=False, font=FONT)

    def adder(self):
        self.score += 1
        self.clear()
        self.updater()
