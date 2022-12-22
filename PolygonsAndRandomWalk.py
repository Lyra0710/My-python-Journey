from turtle import Turtle, Screen
import random


Timmy = Turtle()
screen = Screen()
screen.colormode(255)
Timmy.hideturtle()
Timmy.pensize(5)
list_C = ["indigo", "blue", "deep sky blue", "lawn green", "gold", "dark orange", "red", "violet"]
Timmy.speed("fastest")
screen.screensize(1000,1000)
screen.bgcolor("black")

#Square
# for _ in range(4):
#     Timmy.forward(100)
#     Timmy.right(90)

#Dashed line
# for _ in range (5):
#     Timmy.forward(10)
#     Timmy.penup()
#     Timmy.forward(10)
# Timmy.pendown()

#Triangle
# for x in range(3, 10):
#    Timmy.forward(100)
#    Timmy.right(360/x)

#Triangle to Decagon with diff colors
# for x in range(3, 11):
#     Timmy.color(list_C[x-3])
#     for y in range(x):
#         Timmy.forward(100)
#         Timmy.right(360/x)







#Random walk
# def random_walk():
#     direction_choice = [0,90,270]
#     choice = [-10, 10]
#
#     for y in range(500):
#         Timmy.forward(random.choice(choice))
#         Timmy.color(random.choice(list_C))
#         a = random.choice(direction_choice)
#         Timmy.setheading(random.choice(direction_choice))
# random_walk()

#Random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

direction_choice = [0,90,270]
choice = [-30, 30]

for y in range(500):
    Timmy.color(random_color())
    Timmy.forward(random.choice(choice))
    Timmy.setheading(random.choice(direction_choice))




















screen = Screen()
screen.exitonclick()