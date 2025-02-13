from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # print(ball.ycor(), ball.heading(), sep='|')
    if ball.ycor() > 280 or ball.ycor() < -280:
        # change ball direction
        ball.bounce_y()
        # is_game_on = False

    # detect left/right paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 380:
        scoreboard.increment_left_point()
        ball.reset()

    # detect left paddle miss
    if ball.xcor() < -380:
        scoreboard.increment_right_point()
        ball.reset()

screen.exitonclick()
