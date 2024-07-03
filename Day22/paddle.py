import turtle

class Paddle(turtle.Turtle):

    def __init__(self, x_pos, y_pos):

        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=7)
        self.shape("square")
        self.goto(x_pos, y_pos)
        
    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
