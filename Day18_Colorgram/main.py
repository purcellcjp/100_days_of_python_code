import turtle as t
import os
import random

# import colorgram

os.system('cls')

# rgb_colors = []

# colors = colorgram.extract('hirst.jpg', 40)
# print(len(colors))

# for color in colors:
#     # print(f"{i}. RGB: {color.rgb}, HSL: {color.hsl}, Proportion: {color.proportion}")
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# # for t in rgb_colors:
# #     print(t)

# print(rgb_colors)

color_list = [(236, 251, 243), (200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7),
              (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161), (4, 68, 41), (249, 8, 43), (88, 228, 238), (178, 179, 232), (4, 246, 225), (29, 46, 233), (8, 77, 113), (0, 244, 254), (247, 12, 9)]

# print(len(color_list))


t.colormode(255)


def draw_grid_of_dots(turtle, dot_size, dot_distance, num_rows, num_cols):
    for _ in range(num_rows):
        for _ in range(num_cols):
            turtle.dot(dot_size, random.choice(color_list))
            turtle.forward(dot_distance)
        turtle.backward(dot_distance * num_cols)
        turtle.right(90)
        turtle.forward(dot_distance)
        turtle.left(90)


my_screen = t.Screen()
tt = t.Turtle()

tt.speed('fastest')
tt.penup()
tt.hideturtle()

dot_size = 20
dot_distance = 50
num_rows = 10
num_cols = 10

# center grid
start_x = - (num_cols - 1) * dot_distance / 2
start_y = (num_rows - 1) * dot_distance / 2

tt.goto(start_x, start_y)

draw_grid_of_dots(tt, dot_size, dot_distance, num_rows, num_cols)

my_screen.exitonclick()
