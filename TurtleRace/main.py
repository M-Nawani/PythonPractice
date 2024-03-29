from turtle import Turtle, Screen
import random

myscreen = Screen()
myscreen.setup(width=500, height=400)
user_bet = myscreen.textinput(title="Make your Bet", prompt="Which turtle will win the race ? Enter a color")

colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle has won the race")
            else:
                print(f"You've lost !! The {winning_color} turtle has won the race")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

myscreen.exitonclick()

