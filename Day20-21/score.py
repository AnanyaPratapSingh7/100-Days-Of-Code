from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.message = f"SCORE : {self.score}"
        
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        
        self.write_message()

        

    def increase_score(self):
        self.score += 1
        self.message = f"SCORE : {self.score}"

        self.write_message()
        
    def write_message(self):
        self.clear()
        self.goto(0, 270)
        self.write(self.message, "center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")