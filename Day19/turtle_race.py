import turtle as t
import random 

screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Bet on Turtle", prompt="Which turtle do you think will win : ")


colors = ["blue", "yellow", "green", "red", "orange", "purple"]

x = -210
y = -160

turtles = []

for chosen_color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(chosen_color)
    new_turtle.goto(x, y)
    y += 50

    turtles.append(new_turtle)

race_on = False

if user_bet:
    race_on = True

while race_on:
    for tur in turtles:
        tur.forward(random.randint(0,10))
        if tur.xcor() >= 210:
            winner = tur.color()[0]
            if winner == user_bet:
                print("Congratulations! You won!")
            else:
                print("Unlucky you!")
            print(f"The winner is the {winner} turtle!")
            race_on = False
            break


screen.exitonclick()