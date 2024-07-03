import colorgram
import turtle as t
import random

colors = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]


# color_palatte = colorgram.extract("image.webp", 30)

# for color in color_palatte:
#     colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))

# print(colors)

t.colormode(255)

turtle = t.Turtle()
screen = t.Screen()

turtle.penup()
turtle.setx(250)
turtle.sety(-250)
turtle.setheading(180)

for n in range(10):
    turtle.setx(250)
    turtle.sety(-250 + n*50)

    for _ in range(10):
        turtle.color(random.choice(colors))
        turtle.dot(10)
        turtle.forward(50)

turtle.hideturtle()

screen.exitonclick()