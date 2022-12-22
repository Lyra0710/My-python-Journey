import colorgram
from turtle import Turtle, Screen
import random
rgb_colors=[]
colors = colorgram.extract('DamianHirst.jpeg', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("circle")
tim.hideturtle()
tim.speed("fastest")

list = [(239, 222, 206), (21, 116, 159), (241, 214, 224), (223, 159, 89), (209, 130, 155), (213, 233, 220), (160, 59, 96), (118, 173, 201), (213, 74, 103), (206, 222, 235), (34, 129, 88), (213, 162, 16), (171, 18, 46), (126, 182, 156), (228, 73, 57), (230, 200, 123), (7, 105, 67), (166, 75, 42), (233, 164, 181), (57, 164, 134), (31, 166, 185), (239, 168, 157), (13, 52, 90), (156, 210, 191), (25, 59, 122), (6, 92, 108), (177, 184, 218), (81, 26, 53), (147, 209, 219), (10, 71, 45), (108, 118, 172), (178, 22, 15), (76, 93, 19), (73, 31, 24), (245, 199, 2), (254, 10, 27)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.setheading(0)

dots = 100

for x in range (1, dots + 1):
    tim.dot(20, random.choice(list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if x%10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()













screen.exitonclick()












