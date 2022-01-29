import random
import turtle as t
from turtle import Turtle, Screen

t.colormode(255)
tim = Turtle()
# tim.shape("turtle")
# tim.color("red")


# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side in range(3,11):
#     draw_shape(shape_side)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple
#
#
# direction = [0, 90, 180, 270]
#
# for _ in range(100):
#     movement = random.choice(direction)
#     tim.color(random_color())
#     tim.width(5)
#     tim.forward(20)
#     tim.setheading(movement)


for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.right(10)

my_screen = Screen()
my_screen.exitonclick()
