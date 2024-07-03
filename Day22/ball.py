from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self ):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.color("purple")
        self.setheading(randint(0,360))
        self.move_x = 2
        self.move_y = 2

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        
        self.goto(new_x, new_y)

    def bounce_against_wall(self):
        self.move_y *= -1

    def bounce_against_paddle(self):
        self.move_x *= -1

    def reset(self):
        self.goto(0,0)
        self.move_x *= -1