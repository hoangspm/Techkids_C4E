def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t,sz):
    draw_poly(t,3,sz)

import turtle

wn = turtle. Screen()
wn. bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")
tess.speed(-1)

size=100

draw_equitriangle(tess,size)
