from turtle import Turtle

FONT = ('courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(-270, 270)
        self.score_level_up()

    def score_level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)
