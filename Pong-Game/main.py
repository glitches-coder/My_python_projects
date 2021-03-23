from turtle import Screen, colormode
from paddle import Paddle
from ball import Ball
from score_board import ScoreBrd
import time

colormode(255)
s = Screen()
s.setup(width=800, height=600)
s.bgcolor("Black")
s.title("Pong game")
s.tracer(0)
l_pad = Paddle(a=-350, b=0)
l_pad.color(116, 0, 184)
r_pad = Paddle(a=350, b=0)
r_pad.color(100, 223, 223)
b = Ball()
sb = ScoreBrd()
s.listen()
s.onkey(l_pad.paddle_up, "w")
s.onkey(l_pad.paddle_down, "s")
s.onkey(r_pad.paddle_up, "Up")
s.onkey(r_pad.paddle_down, "Down")
game_on = True
while game_on:
    time.sleep(b.move_spd)
    s.update()
    b.move()
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()
    if b.distance(r_pad) < 50 and b.xcor() > 330 or b.distance(l_pad) < 50 and b.xcor() < -330:
        b.bounce_x()
    if b.xcor() > 380:
        b.setpos(x=0, y=0)
        b.move_spd = 0.1
        b.bounce_x()
        sb.l_update()
    if b.xcor() < -380:
        b.setpos(x=0, y=0)
        b.move_spd = 0.1
        b.bounce_x()
        sb.r_update()

s.exitonclick()
