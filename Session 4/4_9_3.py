def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

import turtle

wn = turtle. Screen()
wn. bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")
tess.pensize(3)
tess.speed(-1)

n=8
size=20

draw_poly(tess,n,size)
