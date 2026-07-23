from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
from constants import *

screen=Screen()
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle=Paddle()
ball=Ball()
score=Scoreboard(LIVES)

colors=['red','orange','yellow','green','blue']
bricks=[]
sx=-360
sy=250

for r in range(ROWS):
    for c in range(COLS): 
        bricks.append(Brick(sx+c*80,sy-r*30,colors[r%5]))

screen.listen()
screen.onkeypress(paddle.move_left,'Left')
screen.onkeypress(paddle.move_right,'Right')

game_on=True
while game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.xcor()>430 or ball.xcor()<-430: 
        ball.bounce_x()
    if ball.ycor()>330: 
        ball.bounce_y()
    if ball.distance(paddle)<55 and ball.ycor()<-280: 
        ball.bounce_y()
    for b in bricks[:]:
        if ball.distance(b)<35:
            b.hideturtle()
            bricks.remove(b)
            ball.bounce_y()
            ball.speed_up()
            score.add_score()
            break
    if ball.ycor()<-340:
        score.lose_life()
        if score.lives==0: 
            score.game_over('GAME OVER')
            game_on=False
        else: 
            ball.reset_ball()
    if not bricks: 
        score.game_over('YOU WIN!')
        game_on=False
screen.exitonclick()
