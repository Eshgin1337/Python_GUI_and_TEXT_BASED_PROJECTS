from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue", "green", "yellow", "orange", "red"]
all_turtles = []
y_coordinate = -70

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    new_turtle.color(colors[i])
    y_coordinate += 35
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You won! The {winning_color} turtle is winner.")
            else:
                print(f"Unfortunately you lost! The {winning_color} turtle is winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
