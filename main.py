from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle(position=(-350, 0), up_key="w", down_key="s")
right_paddle = Paddle(position=(350, 0), up_key="Up", down_key="Down")

pong_ball = Ball()

scoreboard = Scoreboard()

starting_direction = random.choice(pong_ball.direction)
game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    starting_direction()

    # Detect collision with wall
    if pong_ball.ycor() > 270 or pong_ball.ycor() < -270:
        pong_ball.bounce_on_y()

    # Detect collision with paddle
    if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_on_x()


    # Detect if ball misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()

