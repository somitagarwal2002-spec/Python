from turtle import Turtle
from constants import PADDLE_MOVE
class Paddle(Turtle):
    def __init__(self):
        super().__init__('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color('white')
        self.penup()
        self.goto(0,-300)

    def move_left(self): 
        self.setx(self.xcor()-PADDLE_MOVE)

    def move_right(self): 
        self.setx(self.xcor()+PADDLE_MOVE)
