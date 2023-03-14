import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

timmy = Turtle()
# timmy.shape('arrow')
# timmy.color('blue')
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# for i in range(3, 11):
#     edges = i
#     timmy.color(random.choice(colors))
#
#     for _ in range(edges):
#         # timmy.color(random.choice(colors))
#         total = 360
#         timmy.forward(100)
#         timmy.right(total/edges)


timmy.shape('arrow')
direction = [0, 90, 180, 270]
timmy.pensize()
timmy.speed('fastest')


def colors():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#
# for _ in range(200):
#     timmy.forward(30)
#     timmy.color(colors())
#     timmy.right(random.choice(direction))


for _ in range(100):
    timmy.color(colors())
    timmy.circle(70)
    timmy.right(3.6)


screen = Screen()
screen.exitonclick()
