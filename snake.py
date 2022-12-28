from turtle import Turtle

Coordinates = [(0, 0), (-20, 0), (-40, 0)]
move_d = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move()


    def create_snake(self):
        for t in Coordinates:
            new = Turtle("square")
            new.color("white")
            new.speed("fastest")
            new.penup()
            new.goto(t)
            self.segments.append(new)

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.segments[0].forward(move_d)


