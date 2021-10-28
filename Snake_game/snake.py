from turtle import Turtle
#
#
# def game_over():
#     announcement = Turtle()
#     announcement.hideturtle()
#     announcement.penup()
#     announcement.pencolor("yellow")
#     announcement.write("Game Over!", align="Center", font=("courier", 30, "bold"))


class Snake:
    def __init__(self):
        self.segments = []
        self.coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()

    def create_snake(self):
        for i in self.coordinates:
            self.add_segment(i)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend_length(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(20)
