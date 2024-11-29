from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")


    def game_over(self):
        self.write("Game Over", align="center", font=FONT)
