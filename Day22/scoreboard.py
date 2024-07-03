from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(0,220)
        self.color("white")
        self.update()


    def update(self, str=""):
        if str=='left':
            self.l_score+=1
        elif str =='right':
            self.r_score+=1
        
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", False, align="center", font=("Arial", 50, "bold"))
