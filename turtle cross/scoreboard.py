from turtle import Turtle
FONT = ("Courier", 17, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-220, 260)
        self.level = 0
        self.hideturtle()
        self.updater()

    def updater(self):
        self.write(f"Level = {self.level}", align="center", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", move=False, font=FONT)

    def adder(self):
        self.level += 1
        self.clear()
        self.updater()
