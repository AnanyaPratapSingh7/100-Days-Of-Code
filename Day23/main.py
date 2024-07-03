from turtle import Screen
from player import Player
from car import CarManager
from time import sleep
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crosssing")
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkey(key='Up', fun=player.move)

game_on = True



while game_on:
    
    # Running Cars
    car_manager.run()

    # Check if Player crossed finish line
    if player.ycor()>320:
        player.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()

    # Detect collision with car
    for car in car_manager.car_list:
        if player.distance(car) <=30 and player.ycor()<car.ycor()+10:
            game_on = False
            scoreboard.game_over()



    sleep(0.01)
    screen.update()

screen.exitonclick()