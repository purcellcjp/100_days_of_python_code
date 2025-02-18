import pandas as pd
import turtle as t
import csv

ALIGN = 'center'
FONT = ('Courier', 8, 'normal')

score = 0

screen = t.Screen()
screen.setup(width=800, height=800)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)

# func to get x,y coordinates of state location on turtle screen


def get_mouse_click_coor(x, y):
    print('coordinates:', x, y)


t.onscreenclick(get_mouse_click_coor)

# # states_df = pd.read_csv('50_states.csv')
# states_list = []
# state_dict = {}

# with open('50_states.csv') as data_file:

#     reader = csv.reader(data_file)
#     next(reader)    # skip header
#     for row in reader:
#         state = row[0]
#         x = row[1]
#         y = row[2]
#         state_dict = {'state': state, 'x': x, 'y': y}
#         states_list.append(state_dict)
# # print(states_list)

dtype_mapper = {'state': 'string',
                'x': 'float64',
                'y': 'float64'
                }
states_df = pd.read_csv('50_states.csv', dtype=dtype_mapper)
# Load state names to list from dataframe
all_states = states_df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    title_score = f'{score}/50 Correct'
    answer_state = screen.textinput(title=title_score,
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        # export list of states not guessed
        not_guessed = []
        for state in all_states:
            if state not in guessed_states:
                not_guessed.append(state)

        df = pd.DataFrame(not_guessed, columns=['state'])
        df.to_csv('states_to_learn.csv', index=False)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_df = states_df[states_df.state == answer_state]
        label = t.Turtle()
        label.hideturtle()
        label.penup()
        print(answer_state, state_df.x.item(), state_df.y.item(), sep='|')
        # label.goto(state_df.x.item(), state_df.y.item())
        label.goto(280, 280)
        t.write(answer_state, align=ALIGN, font=FONT)
        print('position', label.pos())
        score += 1


# t.mainloop()
