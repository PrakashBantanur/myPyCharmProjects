from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_scores()

    # Detect collision to the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # If snake head hits own tail
    for segments in snake.segments[1:]:
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
