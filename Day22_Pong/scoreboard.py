from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGN, font=FONT)

    def increment_left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def increment_right_point(self):
        self.right_score += 1
        self.update_scoreboard()
