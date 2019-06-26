#Space Invaders game
#By Ariz Chang

import turtle
import os

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

#Draw border
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-300, -300)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
    borderPen.fd(600)
    borderPen.lt(90)
borderPen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 20

#Create the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_wid = 1, stretch_len = .2)
bullet.hideturtle()
bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2

#moves player left
def goLeft():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#moves player right
def goRight():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fireBullet():
    global bulletstate
    if bulletstate == "ready":
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()
        bulletstate = "fire"

#Key bindings
window.listen()
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")
window.onkeypress(fireBullet, "space")

#Main game loop
while True:
    #Move the enemy
    x = enemy.xcor()
    y = enemy.ycor()
    x += enemyspeed
    enemy.setx(x)
    if abs(x) > 280:
        y -= 20
        enemy.sety(y)
        enemyspeed *= -1

    #Move the player bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if bullet has gone to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

