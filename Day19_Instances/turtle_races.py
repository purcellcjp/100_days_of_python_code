import turtle as t
import random

is_race_on = False

my_screen = t.Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(
    title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_turtles = []

y_positions = [-100, -50, 0, 50, 100, 150]

for turtle_index in range(len(colors)):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

# move the turtles randomly
# for _ in range(50):
#     for each_turtle in all_turtles:
#         rand_distance = random.randint(1, 10)
#         each_turtle.forward(rand_distance)


if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 225:
            is_race_on = False
            winning_color = each_turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print('You won!!!')
            else:
                print('You lost!!!')
            print(f'The winning color was {winning_color}.')

        rand_distance = random.randint(1, 10)
        each_turtle.forward(rand_distance)


my_screen.exitonclick()
