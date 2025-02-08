import turtle as t

tt = t.Turtle()
my_screen = t.Screen()


def move_forward():
    tt.forward(10)


def move_backwards():
    tt.backward(10)


def turn_right():
    tt.right(10)


def turn_left():
    new_heading = tt.heading() + 10
    tt.setheading(new_heading)


def clear_screen():
    tt.clear()
    tt.penup()
    tt.home()
    tt.pendown()


my_screen.listen()
my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_backwards)
my_screen.onkey(key='a', fun=turn_left)
my_screen.onkey(key='d', fun=turn_right)
my_screen.onkey(key='c', fun=clear_screen)

my_screen.exitonclick()
