# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
painter = trtl.Turtle()
wn = trtl.Screen()
import random as rng



#-----game configuration----
spot_shape = "circle"
size = 2
circle_color = "pink"
count = 1000
timer_up = False
timer = 30
tsize = 7



#-----initialize turtle-----
painter.shape(spot_shape)
painter.fillcolor(circle_color)
painter.shapesize(size)

#-----game functions--------

def countdown():
  global timer, timer_up
  painter.clear()
  if timer <= 0:
    painter.write("Time's Up", font=5)
    timer_up = True
  else:
    painter.write("Timer: " + str(timer), font=5)
    timer -= 1
    painter.getscreen().ontimer(countdown, count)


def when_clicked(i, j):
    global timer, tsize
    if (timer_up == False):
        painter.color("Red")
        painter.stamp()
        painter.color("blue")
        tsize -= .03
        painter.shapesize(7)
        change_position()
    else:
        painter.hideturtle()

#-----events----------------

def  change_position():
    new_xpos = rng.randint(-200, 200)
    new_ypos = rng.randint(-150, 150)
    painter.goto(new_xpos, new_ypos)

painter.onclick(when_clicked)
wn.ontimer(countdown, count) 
wn.mainloop()
