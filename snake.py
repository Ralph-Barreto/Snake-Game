from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

INITIAL_COORDINATES= [(0, 0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake_part(self, starting_point):
        snake_part = Turtle()
        snake_part.goto(starting_point)
        snake_part.shape("square")
        snake_part.color("green")
        snake_part.penup()
        snake_part.speed("fastest")
        self.snake_body.append(snake_part)

    def create_snake(self):
        for s in INITIAL_COORDINATES:
            self.create_snake_part(s)

    def move(self):
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part - 1].xcor()
            new_y = self.snake_body[body_part - 1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
