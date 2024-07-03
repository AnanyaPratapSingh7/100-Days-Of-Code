from turtle import Turtle
import random

STARTING_SPEED = 1
INCREMENT_SPEED = 1
COLOR = ["orange","red","yellow","green","purple","pink"]
          
class Car(Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLOR))
        self.car_speed = car_speed
        
        x_cor = 320
        y_cor = random.randint(-250, 250)

        self.goto(x_cor, y_cor)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.forward(self.car_speed)



class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_SPEED
        

    def run(self):
        for car in self.car_list:
           car.move()

           if car.xcor()<-320:
               self.car_list.remove(car)

        if random.randint(1,20) == 1:
            self.produce_cars()

    def produce_cars(self):
        new_car = Car(self.speed)
        self.car_list.append(new_car)

    def increase_speed(self):
        self.speed += INCREMENT_SPEED