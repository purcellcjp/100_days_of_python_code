import turtle as t
import random
import time

START_MOVE_DISTANCE = 5
MOVE_DISTANCE_INCREMENT = 10


class Cars():
    def __init__(self):
        self.all_cars = []
        t.colormode(255)
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        # Need to slow car generation
        random_chance = random.randint(1, 6)
        # Only create cars 1/6
        if random_chance == 1:
            new_car = t.Turtle(shape='square')
            new_car.color(self.return_random_color())
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(self.return_random_position())
            # new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_DISTANCE_INCREMENT

    def return_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def return_random_position(self):
        x = 300
        random_y = random.randint(-250, 250)
        return (x, random_y)
