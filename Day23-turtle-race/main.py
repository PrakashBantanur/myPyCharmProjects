import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.car_move()

    # Detect the collision to cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            turtle.write('Game Over!', align='center', font=('center', 15, 'normal'))

    # Detect the finishline
    if player.is_finished():
        player.go_to_start()
        cars.level_up()
        scoreboard.score_level_up()


screen.exitonclick()
