from turtle import Screen
import time
from cars import Cars
from player import Player
from level import Level

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = Cars()
screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
level = Level()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detecting the turtle's collision with the finish line
    if player.ycor() > 280:
        player.reset_position()
        level.level_increase()
        cars.increase_car_speed()

    # Detecting turtle's collision with car
    for car_now in cars.all_cars:
        if car_now.distance(player) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()
