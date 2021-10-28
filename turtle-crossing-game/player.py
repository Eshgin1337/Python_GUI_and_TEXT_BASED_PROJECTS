from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def go_starting(self):
        self.goto(STARTING_POSITION)
