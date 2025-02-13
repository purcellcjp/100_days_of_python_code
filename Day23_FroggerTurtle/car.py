import turtle as t
import random
import time

MOVE_DISTANCE = 10


class Car(t.Turtle):
    def __init__(self, main_screen):
        super().__init__()
        t.colormode(255)
        self.screen = main_screen
        self.color(self.return_random_color())
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.shape('square')
        self.penup()
        self.goto(self.return_random_position())
        self.setheading(180)

    def move_left(self):
        # call move_up every 100 ms
        self.screen.ontimer(self.forward(MOVE_DISTANCE), 100)

    def stop_moving(self):
        self.screen.ontimer(None)

        # while True:
        #     self.car.forward(MOVE_DISTANCE)
        #     time.sleep(1)
        # if self.car.xcor() < -300:
        #     self.car.goto(280, self.car.ycor)
        #     self.screen.update()

    def return_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def return_random_position(self):
        x = 280
        y = random.randint(-260, 280)
        return (x, y)
