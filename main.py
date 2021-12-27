from turtle import Turtle, Screen
import pandas

text = Turtle()
text.hideturtle()

# sets the screen
turtle = Turtle()
screen = Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# manage csv data
state_data = pandas.read_csv("50_states.csv")
states_col = state_data["state"]

score = 0
guessed_states = []
on = True
while on:
    answer_state = screen.textinput(title="type a state or \'exit\'", prompt=f"{score}/50 States Correct!").title()
    for state in states_col:
        if answer_state == "Exit":
            on = False
            break
        if answer_state == state and answer_state not in guessed_states:
            text.penup()
            x = int(state_data[states_col == answer_state].x)
            y = int(state_data[states_col == answer_state].y)
            text.goto(x, y)
            text.pendown()
            text.pencolor("black")
            text.write(f"{state}")
            score += 1
            guessed_states.append(answer_state)

# outputs not guessed files as a CSV
states_list = states_col.to_list()
not_guessed = [state for state in states_col if state not in guessed_states]
not_guessed_df = pandas.DataFrame(not_guessed)
not_guessed_df.to_csv("states_to_learn.csv")





