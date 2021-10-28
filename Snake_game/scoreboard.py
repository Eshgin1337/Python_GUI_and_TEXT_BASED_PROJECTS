from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highest_score = int(f.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.highest_score}", align="center", font=("courier", 14, "normal"))

    def increase_length(self):
        self.score += 1
        self.update_score_board()

    def reset_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score_board()


