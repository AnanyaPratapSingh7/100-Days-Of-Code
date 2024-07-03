from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(-270, 270)
        self.hideturtle()
        self.write_score()

    def increase_level(self):
        self.level+=1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", False, "left", ("Montana", 14, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center",("Arial", 30, "bold"))