import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What is the name of another state?").title()

    if answer_states == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
        
    if answer_states in states:
        guessed_states.append(answer_states)
        write_state = turtle.Turtle()
        write_state.hideturtle()
        write_state.penup()
        x_values = int(data[data.state == answer_states].x)
        y_values = int(data[data.state == answer_states].y)
        state_coords = (x_values, y_values)
        write_state.goto(state_coords)
        write_state.write(f"{answer_states}")





turtle.mainloop()
