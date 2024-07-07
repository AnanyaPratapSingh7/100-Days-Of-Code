from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        
        super().__init__(shape='circle')
        self.color("blue")
        self.penup()
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        xcord = random.randint(-280, 280)
        ycord = random.randint(-280, 280)

        self.goto(xcord, ycord)