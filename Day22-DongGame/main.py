from turtle import Screen, Turtle
from paddle import Peddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
paddle = Turtle()

screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Dong')
screen.tracer(0)

r_paddle = Peddle((350, 0))
l_paddle = Peddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball needs to bounce
        ball.y_bounce()

    # Detect ball collied with paddle
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    # Detect paddle misses the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_count()

    # Detect paddle misses the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_count()


screen.exitonclick()
