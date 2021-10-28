from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # scoreboard.display_highest_score()

    # Detecting if the snake has reached the food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_length()
        snake.extend_length()

    # Detecting collision with the wall
    snake_x_cor = snake.segments[0].xcor()
    snake_y_cor = snake.segments[0].ycor()
    if snake_x_cor > 280 or snake_x_cor < -280 or snake_y_cor < -280 or snake_y_cor > 280:
        scoreboard.reset_highest_score()
        snake.reset_snake()

    # Detecting collusion with the tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset_highest_score()
            snake.reset_snake()

screen.exitonclick()

