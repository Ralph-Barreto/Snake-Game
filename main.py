from turtle import Screen
import time
from snake import Snake
from food import Food
from userinterface import UserInterface

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_body = []

snake = Snake()
food = Food()
UI = UserInterface()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

# detect collision with food
    if snake.head.distance(food) < 15:
        UI.score_increase()
        print(UI.score)
        snake.extend()
        food.refresh()

    # detect collision with wall
    snake_head_xcor = float(snake.head.xcor())
    snake_head_ycor = float(snake.head.ycor())

    if snake_head_xcor > 300 or snake_head_xcor < -300 or snake_head_ycor > 300 or snake_head_ycor < -300:
        print("game over")
        UI.game_over_appear()
        game_is_on = False

    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            UI.game_over_appear()
            game_is_on = False

screen.exitonclick()
