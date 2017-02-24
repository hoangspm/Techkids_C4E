def draw_square(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

import turtle

wn = turtle. Screen()
wn. bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.speed(-1)
tess.pensize(2)

n = 5;
for i in range(n):
    for j in range(4):
        draw_square(tess,40)
        tess.left(90)
    tess.left(18)
