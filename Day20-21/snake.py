from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self, screen):

        self.snake_body = []
        self.screen = screen
    
        self.create_snake()
        self.add_key_bindings()
        self.head = self.snake_body[0]
        self.snake_body[0]

    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            new_segment.speed("slowest")
            self.snake_body.append(new_segment)
        self.screen.update()

    def add_key_bindings(self):
        self.screen.onkeypress(key="w", fun= self.move_up)
        self.screen.onkeypress(key="s", fun= self.move_down)
        self.screen.onkeypress(key="a", fun= self.move_left)
        self.screen.onkeypress(key="d", fun= self.move_right)

    def move_up(self):
        if not self.head.heading()==270:
            self.head.setheading(90)
    def move_left(self):
        if not self.head.heading()==0:
            self.head.setheading(180)
    def move_right(self):
        if not self.head.heading()==180:
            self.head.setheading(0)
    def move_down(self):
        if not self.head.heading()==90:
            self.head.setheading(270)

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        self.snake_body[seg_num-1].forward(20)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.goto(self.snake_body[len(self.snake_body)-1].xcor(), self.snake_body[len(self.snake_body)-1].ycor())
        new_segment.penup()
        new_segment.color("white")
        new_segment.speed("slowest")
        self.snake_body.append(new_segment)