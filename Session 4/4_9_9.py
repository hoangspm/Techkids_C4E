def draw_star(t,sz):
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

draw_star(tess,size)
