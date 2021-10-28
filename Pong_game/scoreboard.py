from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def increase_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto((100, 200))
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))


class GameOver(Turtle):
    def __init__(self, winner):
        super().__init__()
        self.color("Yellow")
        self.penup()
        self.hideturtle()
        self.write(f"The winner is {winner}", align="center", font=("courier", 36, "normal"))


