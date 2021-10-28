from turtle import Screen
from paddles import Paddle, MiddleLine
from ball import Ball
import time
from scoreboard import ScoreBoard, GameOver

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
the_ball = Ball()
middle_line = MiddleLine()
max_score = int(screen.textinput("Max score", "What score would you like to maximum?"))

score = ScoreBoard()

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.onkeypress(l_paddle.up, "q")
screen.onkeypress(l_paddle.down, "x")

screen.onkeypress(r_paddle.up, "p")
screen.onkeypress(r_paddle.down, "m")

is_game_on = True
while is_game_on:
    time.sleep(1/the_ball.t)
    screen.update()
    the_ball.move()

    if the_ball.ycor() > 280 or the_ball.ycor() < -280:
        the_ball.bounce_y()

    r_dist = the_ball.distance(r_paddle)
    l_dist = the_ball.distance(l_paddle)
    if (r_dist < 50 and the_ball.xcor() > 320) or (l_dist <= 50 and the_ball.xcor() < -320):
        the_ball.bounce_x()
        the_ball.setheading(360 - the_ball.heading())

    if the_ball.xcor() > 380:
        the_ball.reset_position()
        score.increase_l()
        the_ball.speed_up()

    if score.r_score == max_score:
        is_game_on = False
        winner = GameOver("Player II")
        time.sleep(3)
        break

    if the_ball.xcor() < -380:
        the_ball.reset_position()
        score.increase_r()
        the_ball.speed_up()

    if score.l_score == max_score:
        is_game_on = False
        winner = GameOver("Player I")
        time.sleep(3)
        break

screen.exitonclick()
