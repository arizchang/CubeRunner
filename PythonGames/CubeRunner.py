#Cube Runner
#By Ariz Chang
 
import turtle
import random
import time
import math

#Block class
class Block(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.shapesize(2, 2)
        self.blockSpeed = 3
        self.color("red")
        self.shape("square")
        self.penup()
        self.speed(0)

    #moves the blocks
    def moveBlock(self):
        self.y = self.ycor()
        self.y -= self.blockSpeed
        self.sety(self.y)
    
    def isBottom(self):
        if(self.ycor < -420):
            return True
    
    def isCollision(self, runner):
        distance = math.sqrt(math.pow(self.xcor() - runner.xcor(), 2) + math.pow(self.ycor() - runner.ycor(), 2))
        if distance < 15:
            return True
        else:
            return False

#runner
runner = turtle.Turtle()
runner.speed(0)
runner.shape("triangle")
runner.color("yellow")
runner.shapesize(stretch_wid = 2, stretch_len = 2)
runner.setheading(90)
runner.penup()
runner.goto(0, -350)
runnerspeed = 20

#Make the window and border
window = turtle.Screen()
window.title("Cube Runner")
window.bgcolor("black")
window.setup(width = 800, height = 800)
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-400, 350)
borderPen.pendown()
borderPen.pensize(3)
borderPen.fd(800)
borderPen.hideturtle()
window.tracer(0)

#display score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
score = 0
realscore = 0
pen.write("Score: 0", align = "center", font = ("Courier", 24, "normal"))

#moves player left
def goLeft():
    x = runner.xcor()
    x -= runnerspeed
    if x < -320:
        x = -320
    runner.setx(x)

#moves player right
def goRight():
    x = runner.xcor()
    x += runnerspeed
    if x > 320:
        x = 320
    runner.setx(x)

#Key bindings
window.listen()
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")

blockList = []

#Main game loop
time.sleep(2)
run = True
while run:
    window.update()

    #generates the blocks
    if score%50 == 0:
        for count in range(6):
            block = Block(random.randrange(-380, 380, 1), 335)
            blockList.append(block)

    #Moves the blocks
    for block in blockList:
        block.moveBlock()
        if block.ycor() < -500:
            blockList.remove(block)
            block.clear()
        if block.isCollision(runner):
            for block in blockList:
                block.hideturtle()
            run = False

    #updates the score
    score += 1
    if score%10 == 0:
        realscore += 1
        pen.clear()
        pen.write("Score: {}".format(realscore), align = "center", font = ("Courier", 24, "normal"))