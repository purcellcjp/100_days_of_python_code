import random

# basic import
# import turtle

# preferred import method when using an object many times in code
# from turtle import Turtle, Screen

# import method to bring in all objects
# This method makes it hard to understand where code objects are coming from
# from turtle import *

# Aliasing Modules
# Good for when objects have long names
import turtle as t
# Change Turtle colormode to use rgb 0-255 values
t.colormode(255)


def return_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


colors = ['light steel blue', 'sky blue', 'dark cyan', 'medium spring green',
          'beige', 'gold', 'rosy brown', 'medium violet red', 'medium purple', 'navy']

my_turtle = t.Turtle()
my_turtle.shape('turtle')
my_turtle.color('magenta', 'green')


def draw_turtle_design():
    for steps in range(25):
        for c in ('blue', 'red', 'green'):
            my_turtle.color(c)
            my_turtle.forward(steps)
            my_turtle.right(30)


def draw_turtle_square():
    # Draw a square
    # my_turtle.forward(50)

    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(50)


def draw_turtle_square_better():
    # Better way to draw square
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


def draw_turtle_dashed_line(length, dash_length=10):
    for i in range(length // (2 * dash_length)):
        my_turtle.pendown()
        my_turtle.forward(dash_length)
        my_turtle.penup()
        my_turtle.forward(dash_length)


def draw_turtle_multiple_shapes():
    i = 0
    colors = ['light steel blue', 'sky blue', 'dark cyan', 'medium spring green',
              'beige', 'gold', 'rosy brown', 'medium violet red', 'medium purple', 'navy']
    # draw shapes with 3 to 10 sides
    for sides in range(3, 11):
        angle = 360 / sides
        my_turtle.color(colors[i])
        # increment shape count
        i += 1

        for i in range(sides):
            my_turtle.forward(100)
            my_turtle.right(angle)


def draw_random_walk(length):
    direction = ['right', 'left']
    my_turtle.width(10)

    for _ in range(100):
        for c in colors:
            my_turtle.color(c)

            random_choice = random.choice(direction)
            if random_choice == 'left':
                walk_left(length=length)
            else:
                walk_right(length=length)


def walk_right(length):
    my_turtle.right(90)
    my_turtle.forward(length)


def walk_left(length):
    my_turtle.left(90)
    my_turtle.forward(length)


def draw_random_walk_solution(length):
    directions = [0, 90, 180, 270]

    my_turtle.width(15)
    my_turtle.speed('fastest')

    for _ in range(100):
        heading = random.choice(directions)
        # my_turtle.color(random.choice(colors))
        my_turtle.color(return_random_color())
        my_turtle.setheading(heading)
        my_turtle.forward(length)


def draw_spirograph(gap_size):

    my_turtle.pensize(2)
    my_turtle.speed('fastest')

    # iterate 6 times
    for i in range(360 // gap_size):
        my_turtle.color(return_random_color())
        my_turtle.circle(100)
        # my_turtle.left(10)
        my_turtle.setheading(my_turtle.heading() + gap_size)

    my_turtle.hideturtle()


# draw_turtle_square_better()
# draw_turtle_dashed_line(800)
# draw_turtle_multiple_shapes()
# draw_random_walk(100)
# draw_random_walk_solution(30)
draw_spirograph(5)


my_screen = t.Screen()
my_screen.exitonclick()
