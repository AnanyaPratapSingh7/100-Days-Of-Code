from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)

screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)



game_on = True

while game_on:

    # Detect collision with ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_against_wall()

    # Detect collision with paddle
    if (ball.distance(paddle1)<70 and ball.xcor()>330) or (ball.distance(paddle2)<70 and ball.xcor()<-330):
        ball.bounce_against_paddle()

    #Detect miss
    if ball.xcor()>400:
        scoreboard.update("left")
        ball.reset()
    elif ball.xcor()<-400:
        scoreboard.update("right")
        ball.reset()

    ball.move()

    time.sleep(0.005)
    screen.update()

screen.exitonclick()