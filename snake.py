from turtle import Turtle
Coordinates = [(0, 0), (-20, 0), (-40, 0)]
move_d = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.Head = self.segments[0]

    def create_snake(self):
        for t in Coordinates:
            self.add(t)

    def add(self, t):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(t)
        self.segments.append(new)

    def incr(self):
        self.add(self.segments[-1].position())

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.Head.forward(move_d)

    def up(self):
        if self.Head.heading() != DOWN:
            self.Head.setheading(UP)

    def down(self):
        if self.Head.heading() != UP:
            self.Head.setheading(DOWN)

    def left(self):
        if self.Head.heading() != RIGHT:
            self.Head.setheading(LEFT)

    def right(self):
        if self.Head.heading() != LEFT:
            self.Head.setheading(RIGHT)

