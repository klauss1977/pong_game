from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed('fastest')

    def move_up(self):
        new_position = (self.xcor(), self.ycor() + DISTANCE)
        self.goto(new_position)

    def move_down(self):
        new_position = (self.xcor(), self.ycor() - DISTANCE)
        self.goto(new_position)


class RightPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(350, 0)


class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(-350, 0)
