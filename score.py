from turtle import Turtle
alignment = 'center'
font_style = ('bauhaus 93', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 190)
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align= alignment, font=font_style)

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=alignment, font= font_style)

    def finish(self):
        self.goto(0, 0)
        self.write('GAME OVER', align= alignment, font= font_style)
    def score_incr(self):
        self.score += 1
        self.clear()
        self.update_score()
