from turtle import Turtle
import random

COLORS = ["red", "blue", "orange", "yellow", "purple", "pink", "green"]
STARTING_MOVE_DISTANCE = 5
INCREMENT_DISTANCE = 10


class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_movement = random.randint(1,6)
        if random_movement == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += INCREMENT_DISTANCE



