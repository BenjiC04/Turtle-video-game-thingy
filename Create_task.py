#imports
import turtle
trtl = turtle
import random
import time
from turtle import *

#setup pac
wn = trtl.Screen()
score_board = trtl.Turtle()
t = trtl.Turtle()
a = trtl.Turtle()
border=trtl.Turtle()
border.speed(0)
t.speed(0)
t.penup()
wn.setup(width = 1000, height = 800)
score = 0


#creating indiviual borders

border.penup()
border.color("blue")
border.setposition(-300, -300)
border.pendown()
border.pensize(10)
for i in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

#apple setup

apple = ['apple.gif', 'apple2.gif', 'apple3.gif', 'apple4.gif', 'apple5.gif']
r = random.randint(0, 4)
wn.addshape(apple[r])
a.shape(apple[r])
a.speed(0)
a.penup()
a.goto(random.randint(-300, 300),random.randint(-300, 300))    

#pac controls
wn.addshape('pac2.gif')
t.shape('pac2.gif')

def up():
    t.setheading(90)

def down():
    t.setheading(270)

def left():
    t.setheading(180)

def right():
    t.setheading(0)
    

turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

def coordinate():
    t.pencolor('yellow')
    p = t.pos()
    t.write(str(p), True)
    t.penup()

turtle.onkey(coordinate, 'a')


#pac bounces off borders
while True:
    t.forward(5)
    if t.xcor() > 300 or t.xcor() < -300:
        t.right(180)
    
    if t.ycor() > 300 or t.ycor() < -300:
        t.right(180)
    wn.update()

    #apple color after eaten

    if t.distance(a) < 45:
        apple = ['apple.gif', 'apple2.gif', 'apple3.gif', 'apple4.gif', 'apple5.gif']
        r = random.randint(0, 4)
        wn.addshape(apple[r])
        a.shape(apple[r])
        a.goto(random.randint(-300, 300),random.randint(-300, 300))

        score = score + 1
        score_board.penup()
        score_board.clear()
        score_board.hideturtle()
        score_board.setposition(0, 350)
        update_score ="Score: %s" % score
        score_board.write(update_score, False, align='center', font=('Ariel', 20, 'normal'))
        



turtle.mainloop()

