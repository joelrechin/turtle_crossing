import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.drive()
    cars.new_car()
    if player.ycor() > 280:
        scoreboard.increase_point()
        player.reset()
        cars.x_move *= 1.25
    for car in cars.cars:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


