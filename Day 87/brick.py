from turtle import Turtle
class Brick(Turtle):
    def __init__(self,x,y,color):
        super().__init__('square') 
        self.shapesize(stretch_wid=1,stretch_len=3.5) 
        self.color(color)
        self.penup()
        self.goto(x,y)
