import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_guesses = []

while len(correct_guesses) <= 50:
    placer = turtle.Turtle()
    placer.penup()
    placer.hideturtle()
    state = screen.textinput(title=f"{len(correct_guesses)}/50 Correctly Guessed. ",
                             prompt="What is another state? ").title()

    if state == "Exit":
        missing_states = [i for i in states_list if i not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_tp_learn.csv")
        break

    if state not in correct_guesses:
        if state in states_list:
            correct_guesses.append(state)
            line = data[data["state"] == state]
            placer.goto(int(line.x), int(line.y))
            placer.write(f"{state}")

