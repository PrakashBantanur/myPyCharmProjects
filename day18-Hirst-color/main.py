import turtle

# import colorgram

from turtle import Turtle, Screen
import random
turtle.colormode(255)

# color_pallet = []
# colors = colorgram.extract('61RQCX9SJKL.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extract = (r, g, b)
#     color_pallet.append(extract)
#
# print(color_pallet)

new_colors = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
              (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44),
              (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23),
              (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182),
              (180, 187, 211)]

timmy = Turtle()

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed('fastest')


def hirst_dots(n):
    count = 0
    while count < n:
        for _ in range(n):
            timmy.dot(200/n, random.choice(new_colors))
            timmy.penup()
            timmy.forward(500/n)
            timmy.pendown()

        timmy.penup()
        timmy.setheading(90)
        timmy.forward(500/n)
        timmy.setheading(180)
        timmy.forward((500/n)*n)
        timmy.setheading(0)
        count += 1


hirst_dots(10)

screen = Screen()
screen.exitonclick()
