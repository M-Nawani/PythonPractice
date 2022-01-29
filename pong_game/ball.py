from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_ball_y(self):
        # updating the y-axis of the ball to a smaller value, so that it's back in the screen
        self.y_move *= -1

    def bounce_ball_x(self):
        # updating the x-axis of the ball to a smaller value, so that it's back in the screen
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_ball_x()







