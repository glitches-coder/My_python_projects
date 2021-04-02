import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()
c = CarManager()
scr_brd = Scoreboard()

screen.listen()
screen.onkey(p.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.car_gen()
    c.move()

    for i in c.all_cars:
        if i.distance(p) < 20:
            game_is_on = False
            scr_brd.game_over()

    if p.ycor() > 280:
        p.player_reset()
        c.reset()
        scr_brd.adder()


screen.exitonclick()