import turtle as t


class Snake():
    def __init__(self):
        # Create snake body
        self.snake_body = []
        self.x_position = 0

        for _ in range(3):
            snake = t.Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(x=self.x_position, y=0)
            self.x_position -= 20
            self.snake_body.append(snake)

    def move(self):
        for body_index in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_index - 1].xcor()
            new_y = self.snake_body[body_index - 1].ycor()
            self.snake_body[body_index].goto(new_x, new_y)
        self.snake_body[0].forward(20)
