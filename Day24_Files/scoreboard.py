from turtle import Turtle

DATA_FILE_NAME = 'data.txt'
ALIGN = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.lookup_high_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f'Score: {self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # save new hire score to text file
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER !!!', align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def lookup_high_score(self):
        with open(DATA_FILE_NAME, mode='r') as file:
            cur_high_score = int(file.read())
        return cur_high_score

    def save_high_score(self):
        with open(DATA_FILE_NAME, mode='w') as file:
            file.write(str(self.high_score))
