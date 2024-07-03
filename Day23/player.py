from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(0, -270)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -270)