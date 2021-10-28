import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkSeaGreen")
screen.tracer(0)
player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
game_state = GameOver()

screen.onkeypress(fun=player.go, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    for k in car_manager.all_cars:
        if player.distance(k) < 20:
            game_is_on = False
            game_state.game_over()

    if player.ycor() == 300:
        player.go_starting()
        car_manager.speed_up()
        scoreboard.update_scoreboard()
screen.exitonclick()
