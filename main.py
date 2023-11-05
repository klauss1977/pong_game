import time
from turtle import Screen

from ball import Ball
from paddle import RightPaddle, LeftPaddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = RightPaddle()
left_paddle = LeftPaddle()
ball = Ball()
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkey(screen.bye, "q")

while True:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
