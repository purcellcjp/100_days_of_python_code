from turtle import Turtle
import time

MOVE_DISTANCE = 20


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        # self.screen = main_screen
        self.color('green')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # self.screen.ontimer(self.move_up, 150)  # call move_up every 50 ms

    # def start_moving_up(self):
    #     self.move_up()

    # def stop_moving_up(self):
    #     self.screen.ontimer(None)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())
