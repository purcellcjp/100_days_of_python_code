from turtle import Turtle
POSITION = (-280, 250)
ALIGN = 'left'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f'Level: {self.level}', align=ALIGN, font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over_man(self):
        self.goto(0, 0)
        self.write('GAME OVER MAN !!!', align='center', font=FONT)
