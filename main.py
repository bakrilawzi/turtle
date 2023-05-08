import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("U.s State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []
print(all_state)
is_true = True
while len(guessed_states)<50 and is_true:
    answer_state = str(screen.textinput(title=f"{len(guessed_states)}/50",prompt="enter the guessed state")).title()
    if answer_state=="Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("new_state.csv")
        is_true=False

    if answer_state is all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
