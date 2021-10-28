from colors import colors
import turtle as t
import random

t.colormode(255)
drawer = t.Turtle()
drawer.hideturtle()
screen = t.Screen()
screen.setup(width=600, height=600)
drawer.penup()
drawer.speed("fastest")

initial_y = -250
initial_x = -250

for _ in range(10):
    for _ in range(10):
        drawer.goto(initial_x, initial_y)
        drawer.dot(20, random.choice(colors))
        initial_x = initial_x + 50
    initial_x = -250
    initial_y += 50

screen.exitonclick()
