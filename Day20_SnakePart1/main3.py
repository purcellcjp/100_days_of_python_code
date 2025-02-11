from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# move snake body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect snake collision with food
    # food size is 10 x 10
    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        food.refresh()
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for body in snake.snake_body[1:]:
        # if body != snake.head:
        if snake.head.distance(body) < 10:
            # if snake head collides with tail - game over
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
