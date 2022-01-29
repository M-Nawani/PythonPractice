from turtle import Turtle, Screen

tim = Turtle()
myScreen = Screen()


def turtle_move_forward():
    tim.forward(20)


def turtle_move_backward():
    tim.backward(20)


def turtle_move_left():
    tim.forward(10)
    tim.left(10)


def turtle_move_right():
    tim.forward(10)
    tim.right(10)


def turtle_clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


myScreen.listen()
myScreen.onkey(key="W", fun=turtle_move_forward)
myScreen.onkey(key="S", fun=turtle_move_backward)
myScreen.onkey(key="A", fun=turtle_move_left)
myScreen.onkey(key="D", fun=turtle_move_right)
myScreen.onkey(key="C", fun=turtle_clear_screen)

myScreen.exitonclick()
