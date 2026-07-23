from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__('circle') 
        self.color('white') 
        self.penup(); 
        self.dx=4; 
        self.dy=4; 
        self.move_speed=0.1
    def move(self): 
        self.goto(self.xcor()+self.dx,self.ycor()+self.dy)

    def bounce_x(self): 
        self.dx*=-1

    def bounce_y(self): 
        self.dy*=-1

    def reset_ball(self): 
        self.goto(0,0) 
        self.bounce_y() 
        self.move_speed=0.1

    def speed_up(self): 
        self.move_speed=max(0.03,self.move_speed*0.95)
