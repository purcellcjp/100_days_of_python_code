import turtle as t


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]


class Snake():
    def __init__(self):
        # Create snake body
        self.snake_body = []
        self.x_position = 0
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
            snake = t.Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(position)            
            self.snake_body.append(snake)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for body_index in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_index - 1].xcor()
            new_y = self.snake_body[body_index - 1].ycor()
            self.snake_body[body_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
