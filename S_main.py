import time
from turtle import Turtle, Screen
from snake import Snake

# setting up the game
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

start = True
# Moving the snake body
while start:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()