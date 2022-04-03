from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
NUMBER_OF_CARS = 15

class CarManager():

    def __init__(self):
        self.x_move = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_traffic()

    def add_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto((random.randint(-250, 250), random.randint(-250, 250)))
        return new_car

    def create_traffic(self):
        for _ in range(NUMBER_OF_CARS):
            self.cars.append(self.add_car())

    def drive(self):
        for car in self.cars:
            new_x = car.xcor() - self.x_move
            y = car.ycor()
            car.goto(new_x, y)

    def new_car(self):
        for car in self.cars:
            if car.xcor() < -350:
                index = self.cars.index(car)
                new_car = self.add_car()
                y = new_car.ycor()
                new_car.goto((320,y))
                self.cars[index] = new_car






