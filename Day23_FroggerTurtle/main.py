from turtle import Turtle, Screen
from frog import Frog
from car import Car
import random
import time

all_cars = []


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Frogger via Turtle')
screen.tracer(0)

frog = Frog()


screen.onkey(frog.move_up, 'Up')

# screen.onkeypress(frog.start_moving_up, 'Up')
# screen.onkeyrelease(frog.stop_moving_up, 'Up')


screen.onkey(frog.move_down, 'Down')
# screen.onkey(frog.move_left, 'Left')
# screen.onkey(frog.move_right, 'Right')


screen.listen()

car = Car(main_screen=screen)
car.move_left()

# car = Turtle(shape='square')
# car.penup()
# car.goto(280, 0)

is_game_on = True
i = 0
while is_game_on:
    i += 1
    time.sleep(0.1)
    screen.update()

        


screen.exitonclick()
