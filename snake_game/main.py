from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.bgcolor("black")
myscreen.title("My Snake Game")
myscreen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score = Scoreboard()

myscreen.listen()
myscreen.onkey(fun=snake.up, key="Up")
myscreen.onkey(fun=snake.down, key="Down")
myscreen.onkey(fun=snake.left, key="Left")
myscreen.onkey(fun=snake.right, key="Right")

while game_is_on:
    myscreen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.score_tracker()
        snake.extend_snake()
        food.refresh_position()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() > 280 or snake.head.xcor() < -280:
        score.reset_score()
        snake.reset_snake()

    # Detecting collision with the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

myscreen.exitonclick()
