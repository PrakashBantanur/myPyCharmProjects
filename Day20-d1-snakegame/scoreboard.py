from turtle import Turtle
FONT = ('arial', 14, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.refresh_scores()

    def update_scoreboard(self):
        self.write(f'Score: {self.scores}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!', align='center', font=FONT)

    def refresh_scores(self):
        self.clear()
        self.update_scoreboard()
        self.scores += 1
