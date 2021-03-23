from turtle import Turtle, colormode


class ScoreBrd(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.l_scr = 0
        self.r_scr = 0
        self.update_score()

    def update_score(self):
        colormode(255)
        self.clear()
        self.goto(x=-100, y=200)
        self.color(116, 0, 184)
        self.write(self.l_scr, align="center", font=("OpenSans", 50, "bold"))
        self.goto(x=100, y=200)
        self.color(100, 223, 223)
        self.write(self.r_scr, align="center", font=("OpenSans", 50, "bold"))

    def l_update(self):
        self.l_scr += 1
        self.update_score()

    def r_update(self):
        self.r_scr += 1
        self.update_score()
