import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

# setting up the game
screen = Screen()

screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
Points = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

start = True
# Moving the snake body
while start:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision with food
    if snake.Head.distance(food) < 15:
        food.move_food()
        Points.score_incr()
        snake.incr()

    # Wall collision
    if snake.Head.xcor() > 245 or snake.Head.xcor() < -245 or snake.Head.ycor() > 245 or snake.Head.ycor() < -245:
        start = False
        Points.finish()

    # Tail collision
    for segment in snake.segments[1:]:
        if snake.Head.distance(segment) < 10:
            start = False
            Points.finish()

screen.exitonclick()