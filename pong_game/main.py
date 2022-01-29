from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detecting ball's collision with the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    # Detect if the ball misses the R-paddle
    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.l_points()

    # Detect if the ball misses the L-paddle
    if ball.xcor() < -380:
        ball.reset_ball_position()
        score.r_points()

screen.exitonclick()
