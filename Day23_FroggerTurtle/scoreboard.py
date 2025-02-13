from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()