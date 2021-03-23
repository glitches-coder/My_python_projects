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
        with open("high_score_saver.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.updater()

    def updater(self):
        self.clear()
        self.write(f"Your score is = {self.score}  High Score: {self.high_score}", align=ALIGN, move=False, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_saver.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

        self.updater()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align=ALIGN, move=False, font=FONT)

    def adder(self):
        self.score += 1
        self.updater()
