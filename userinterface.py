from turtle import Turtle

class UserInterface(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 20, "normal"))


    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 20, "normal"))

    def game_over_appear(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))