import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(title='Your bet', prompt='Who will win the turtle race? Guess your turtle color: ')
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']
positions = [-150, -90, -30, 30, 90, 150]
all_turtle = []

is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=positions[turtle_index])
    all_turtle.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won, {winning_color} color turtle won")
            else:
                print(f"You've lost the race, {winning_color} turtle won the race")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
