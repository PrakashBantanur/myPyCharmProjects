import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')


def move_forward():
    tim.setheading(0)
    tim.forward(100)


def move_backward():
    # tim.right(180)
    tim.setheading(180)
    tim.forward(100)


def move_up():
    tim.setheading(90)
    tim.forward(100)


def move_down():
    tim.setheading(-90)
    tim.forward(100)


screen = Screen()
screen.listen()
screen.onkey(key='d', fun=move_forward)
screen.onkey(key='a', fun=move_backward)
screen.onkey(key='w', fun=move_up)
screen.onkey(key='s', fun=move_down)
screen.onkey(key='c', fun=turtle.resetscreen)

screen.exitonclick()
