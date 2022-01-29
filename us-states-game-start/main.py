import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")

state_in_sheet = states["state"].tolist()
guessed_state_list = []

while len(guessed_state_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state_list)}/50 states correct",
                                    prompt="What's another state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_in_sheet if state not in guessed_state_list]
        df = pandas.DataFrame(missing_states, columns=['State'])
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in state_in_sheet:
        guessed_state_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = states.loc[states['state'] == answer_state]
        t.goto(x=int(row.x), y=int(row.y))
        t.write(arg=answer_state, align="left")

# Missing states will go in a csv so user can read all the states they missed
# missing_states = list(set(state_in_sheet).difference(guessed_state_list))







