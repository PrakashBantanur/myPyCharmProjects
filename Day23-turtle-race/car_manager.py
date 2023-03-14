from turtle import Turtle
import random

colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
STARTING_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_DISTANCE

    def create_car(self):
        new_chance = random.randint(1, 6)
        if new_chance == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(colors))
            new_car.turtlesize(1, 2)
            new_car.penup()
            random_y = random.randint(-280, 280)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
