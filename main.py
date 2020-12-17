# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# for col in colors:
#     red = col.rgb.r
#     blue = col.rgb.b
#     green = col.rgb.g
#     color = (red, green, blue)
#     rgb_colors.append(color)
# print(rgb_colors)

import turtle
import random

color_list = [(202, 12, 30),
              (238, 244, 250), (35, 91, 186), (232, 229, 4), (232, 149, 48), (197, 68, 22), (212, 13, 9),
              (35, 31, 152), (49, 220, 60), (241, 46, 151), (20, 22, 53), (14, 208, 224), (75, 9, 53),
              (17, 154, 18), (55, 26, 13), (80, 193, 223), (219, 23, 116), (232, 159, 8), (241, 64, 24),
              (221, 138, 191), (96, 75, 10), (247, 11, 9), (83, 238, 162), (11, 96, 63), (5, 35, 33),
              (89, 208, 147)]

turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.penup()
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
