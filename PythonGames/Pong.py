#Pong
#By Ariz Chang

import turtle
import random

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Score
scoreA = 0
scoreB = 0

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  PLayer B: 0", align = "center", font = ("Courier", 24, "normal"))

#moves paddle A up
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

#moves paddle A down
def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

#moves paddle B up
def paddleBUp():
    y = paddleB.ycor()
    y += 30
    paddleB.sety(y)

#moves paddle B down
def paddleBDown():
    y = paddleB.ycor()
    y -= 30
    paddleB.sety(y)

def startGame():
    if ball.dx == 0:
        ball.dx = .2*(random.choice([1, -1]))
        ball.dy = .2*(random.choice([1, -1]))

#Key bindings
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")
window.onkeypress(startGame, "space")

#Main game loop
while True:
    window.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  PLayer B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        ball.dx = 0
        ball.dy = 0
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  PLayer B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        ball.dx = 0
        ball.dy = 0
        
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

            #Paddle and ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    