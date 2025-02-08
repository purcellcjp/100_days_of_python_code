from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

# Create snake body
snake_body = []
x_position = 0

for _ in range(3):
    snake = Turtle(shape='square')
    snake.color('white')
    snake.penup()
    snake.goto(x=x_position, y=0)
    x_position -= 20
    snake_body.append(snake)

# screen.update()

# move snake body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for body in snake_body:
    #     # body.penup()
    #     body.forward(20)

    for body_index in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[body_index - 1].xcor()
        new_y = snake_body[body_index - 1].ycor()
        snake_body[body_index].goto(new_x, new_y)
    snake_body[0].forward(20)

    # if body.xcor() > 275:
    #     game_is_on = False


screen.exitonclick()
