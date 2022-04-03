from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCREEN_POSITION = (-200,260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(SCREEN_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()