from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")


    def move_food(self):
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        self.penup()
        self.goto(food_x, food_y)