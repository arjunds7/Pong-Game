from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.paddle_go_up, "Up")
screen.onkey(r_paddle.paddle_go_down, "Down")
screen.onkey(l_paddle.paddle_go_up, "w")
screen.onkey(l_paddle.paddle_go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_pace)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.ball_pace *= 0.7

    # Detect if r_paddle misses
    if ball.xcor() > 385:
        ball.reset_position()
        score.l_update_score()

    # Detect if l_paddle misses
    if ball.xcor() < -385:
        ball.reset_position()
        score.r_update_score()

screen.exitonclick()