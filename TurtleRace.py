from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user = screen.textinput(title="What's your bet?",
                        prompt="Enter the color of the turtle that is going to win the race: ")

colors = ["aqua", "purple", "blue", "green", "yellow", "orange"]
a = [0, 30, 60, -30, -60, -90]  # y coordinates of the turtles in the starting position
turtles = []

for t in range(0, 6):
    leo = Turtle("turtle")
    leo.color(colors[t - 1])
    leo.penup()
    leo.goto(x=-240, y=a[t - 1])
    turtles.append(leo)

if user:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user:
                print(f'You won! The {winning_turtle} is the winner!')
            else:
                print("Sorry! You've lost the bet")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
