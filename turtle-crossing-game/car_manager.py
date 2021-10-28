from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_prob = random.randint(1, 6)
        if random_prob == 1:
            random_y = random.randint(-250, 250)
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color(random.choice(COLORS))
            new_turtle.turtlesize(stretch_wid=1, stretch_len=2)
            new_turtle.penup()
            new_turtle.goto(300, random_y)
            self.all_cars.append(new_turtle)

    def move(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
