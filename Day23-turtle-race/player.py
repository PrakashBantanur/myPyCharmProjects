from turtle import Turtle

SET_POSITION = (0, -280)
DISTANCE = 10
FINISHED_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(DISTANCE)

    def move_down(self):
        self.backward(DISTANCE)

    def go_to_start(self):
        self.goto(SET_POSITION)

    def is_finished(self):
        if self.ycor() > FINISHED_LINE_Y:
            return True
        else:
            return False
