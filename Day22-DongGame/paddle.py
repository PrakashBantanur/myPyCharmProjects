from turtle import Turtle


class Peddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.turtlesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
