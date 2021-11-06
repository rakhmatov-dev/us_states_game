import turtle
import pandas

IMAGE_FILE = "blank_states_img.gif"
STATES_FILE = "50_states.csv"
OUTPUT_FILE = "states_to_learn.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(IMAGE_FILE)

turtle.shape(IMAGE_FILE)

state_label_turtle = turtle.Turtle()
state_label_turtle.penup()
state_label_turtle.hideturtle()
state_label_turtle.color("black")

# How to define coordinates of state labels
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(fun=get_mouse_click_coordinates)
#
# turtle.mainloop()
##

df_states = pandas.read_csv(STATES_FILE)
guessed_states = []
while len(guessed_states) < 50:

    try:

        answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?")
        if answer.lower() == "exit":
            break
        if len(df_states[df_states["state"].str.lower() == answer.lower()]) != 0:
            guessed_state = df_states[df_states["state"].str.lower() == answer.lower()]
            state_label_turtle.goto(x=int(guessed_state.x), y=int(guessed_state.y))
            state_label_turtle.write(guessed_state.state.item())
            guessed_states.append(guessed_state.state.item())

    except Exception as err:
        break

# Conditional list comprehension
states_to_learn = [state for state in df_states["state"].to_list() if (state != "state" and state not in guessed_states)]
# for state in df_states["state"].to_list():
#     if (state != "state"
#             and state not in guessed_states):
#         states_to_learn.append(state)

df_output = pandas.DataFrame(states_to_learn)
df_output.to_csv(OUTPUT_FILE)
