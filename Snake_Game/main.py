from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")

sn = Snake()
food = Food()
scr_brd = ScoreBoard()
s.listen()
s.onkey(sn.up, "Up")
s.onkey(sn.down, "Down")
s.onkey(sn.left, "Left")
s.onkey(sn.right, "Right")
s.tracer(0)


game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    sn.move()

    if sn.head.distance(food) < 15:
        food.refresh()
        sn.extender()
        scr_brd.adder()

    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        game_on = False
        scr_brd.game_over()

    for seg in sn.turtles[1:]:
        if sn.head.distance(seg) < 10:
            game_on = False
            scr_brd.game_over()

s.exitonclick()
