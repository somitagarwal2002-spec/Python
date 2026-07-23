from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,lives):
        super().__init__()
        self.score=0
        self.lives=lives
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,320)
        self.update()

    def update(self): 
        self.clear()
        self.write(f'Score: {self.score}   Lives: {self.lives}',align='center',font=('Arial',16,'bold'))

    def add_score(self): 
        self.score+=10
        self.update()

    def lose_life(self): 
        self.lives-=1
        self.update()

    def game_over(self,msg): 
        self.goto(0,0)
        self.write(msg,align='center',font=('Arial',24,'bold'))
