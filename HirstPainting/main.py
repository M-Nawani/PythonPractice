import random
import turtle as turtle_module

import colorgram

# colors = colorgram.extract("hirst.jpg", 16)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

color_list = [(231, 251, 242), (198, 12, 32), (250, 237, 17), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.shape("arrow")
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
should_continue = True

x = 0
y = 0

while should_continue:
    if y == 500:
        should_continue = False
    else:
        while x < 500:
            tim.setposition(x, y)
            tim.penup()
            tim.forward(50)
            tim.dot(20, random.choice(color_list))
            x += 50
        x = 0
        y += 50


myscreen = turtle_module.Screen()
myscreen.exitonclick()




