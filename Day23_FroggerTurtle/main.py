from turtle import Turtle, Screen
from frog import Frog
from cars import Cars
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
screen.onkey(frog.move_left, 'Left')
screen.onkey(frog.move_right, 'Right')


screen.listen()

cars = Cars()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect turtle collision
    for car in cars.all_cars:
        if car.distance(frog) < 20:
            is_game_on = False

    # Detect when frog makes it to top of screen
    if frog.is_at_finish_line():
        frog.go_to_start()
        cars.level_up()
        
        
    # if frog.ycor() > 285:
    #     is_game_on = False

screen.exitonclick()
