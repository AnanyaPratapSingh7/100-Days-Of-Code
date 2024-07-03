from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_left():
    tim.left(5)

def move_right():
    tim.right(5)

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)



screen.onkeypress(key='a', fun = move_left)
screen.onkeypress(key='d', fun = move_right)
screen.onkeypress(key='w', fun = move_forward)
screen.onkeypress(key='s', fun = move_back)
screen.onkeypress(key='c', fun= tim.clear)

screen.exitonclick()