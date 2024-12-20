from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake=Snake()
food= Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_score()
    # Detect collision with the walls and GAME OVER
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()
        game_is_on=False
        scoreboard.game_over()
    # Detect collision with tail

    for block in snake.blocks[1:]:
        if snake.head.distance(block)<10:
            scoreboard.reset()
            snake.reset()
            game_is_on=False
            scoreboard.game_over() 
        
        







screen.exitonclick()