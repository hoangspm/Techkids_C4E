def draw_star(t,sz):
    t.pendown()
    for i in range(5):
        t.forward(100)
        t.right(144)

import turtle

wn = turtle. Screen()
wn. bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")
tess.pensize(2)
tess.speed(-1)

size=100

for i in range(5):
    draw_star(tess,size)
    tess.penup()
    tess.forward(32.5)
    tess.left(72)
    tess.forward(150)
    
