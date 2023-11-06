import time
from turtle import Screen

from ball import Ball
from paddle import RightPaddle, LeftPaddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = RightPaddle()
left_paddle = LeftPaddle()
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkey(screen.bye, "q")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
