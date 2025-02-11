from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
