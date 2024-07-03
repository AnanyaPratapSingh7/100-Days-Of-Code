import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S State Guessing Game")
image = "./US/blank_states_img.gif"
screen.tracer(0)
screen.bgpic(image)


guessed_state = []

data = pd.read_csv("US/50_states.csv")

states = data.state.to_list()
xcor = data.x.to_list()
ycor = data.y.to_list()

pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.hideturtle()

while len(guessed_state)<50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Guess the name of a state : ").title()

    if answer == 'Exit':
        break
    elif answer in states:
        selected_state = data[data.state == answer]

        pen.goto(int(selected_state.x), int(selected_state.y))

        pen.write(answer, False, align="center")

        guessed_state.append(answer)

    screen.update()

states_not_guessed = []

for state in states:
    if state not in guessed_state:
        states_not_guessed.append(state)

df = pd.DataFrame(states_not_guessed)
df.to_csv("Unguessed_states.csv")

turtle.mainloop()