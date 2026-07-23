import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)

bullet = turtle.Turtle()
bullet.shape("square")
bullet.shapesize(0.3, 1)
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

aliens = []

for row in range(3):
    for col in range(8):
        alien = turtle.Turtle()
        alien.shape("circle")
        alien.color("lime")
        alien.penup()
        alien.goto(-280 + col * 80, 200 - row * 60)
        aliens.append(alien)

alien_speed = 2


def move_left():
    x = player.xcor() - 25
    if x > -370:
        player.setx(x)


def move_right():
    x = player.xcor() + 25
    if x < 370:
        player.setx(x)


def fire():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire, "space")

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-380, 260)

game_over = False

while not game_over:

    screen.update()

    pen.clear()
    pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

    edge = False

    for alien in aliens:
        alien.setx(alien.xcor() + alien_speed)

        if alien.xcor() > 360 or alien.xcor() < -360:
            edge = True

        if alien.distance(player) < 25 or alien.ycor() <= -220:
            game_over = True

        if bullet_state == "fire" and bullet.distance(alien) < 20:
            alien.goto(random.randint(-320, 320), random.randint(180, 260))
            bullet.hideturtle()
            bullet_state = "ready"
            score += 10

    if edge:
        alien_speed *= -1
        for alien in aliens:
            alien.sety(alien.ycor() - 20)

    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)

        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullet_state = "ready"

pen.goto(0, 0)
pen.write("GAME OVER", align="center", font=("Arial", 28, "bold"))

screen.update()
screen.mainloop()
