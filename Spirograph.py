from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.screensize(500, 500)
screen.colormode(255)
tim.shape("classic")
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

def spirograph(size_of_gap):
    for x in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(10 + current_heading)


spirograph(5)


screen.exitonclick()