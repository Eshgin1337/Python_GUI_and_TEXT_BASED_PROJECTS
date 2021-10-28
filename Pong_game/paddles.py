from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(coordinates)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.speed(1000)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.speed(1000)


class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(10)
        self.speed("fastest")
        self.penup()
        self.goto(0, -300)
        for _ in range(15):
            new_y = self.ycor() + 20
            self.goto(0, new_y)
            self.pendown()
            new_y = self.ycor() + 20
            self.goto(0, new_y)
            self.penup()

