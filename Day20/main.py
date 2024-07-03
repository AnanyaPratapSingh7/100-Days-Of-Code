from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time 

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake(screen)
food = Food()
scoreboard = Scoreboard()

game_on = True

while game_on:
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    time.sleep(0.075)
    screen.update()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on = False
        scoreboard.game_over()

    for idx in range(1, len(snake.snake_body)-1):
        if snake.head.distance(snake.snake_body[idx])<10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()