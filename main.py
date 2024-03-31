import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)    #To set the size of the screen
screen.title("Pong game")
screen.tracer(0)  # which controls the animation(0 indicate turn of the tracing)

right_paddle = Paddle((350, 0,))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()



screen.listen()
screen.onkey(right_paddle.go_up, "Up")    #when we using function as a parameter we don't want to add parenthesis
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.up, "w")    #when we using function as a parameter we don't want to add parenthesis
screen.onkey(left_paddle.down, "s")

game_on = True
#manually update the screen everytime so we use while loop
while game_on:
    time.sleep(ball.movespeed -0)          # slow down the moving process
    screen.update()
    ball.move()

    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with right_paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340 ) or (ball.distance(left_paddle) < 50 and
                                                                    ball.xcor() < -340):
        ball.bounce_x()

    #if right paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        score.left_point()

    #left side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()









screen.exitonclick()

