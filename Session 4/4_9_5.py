import turtle

wn = turtle. Screen()
wn. bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.speed(-1)

size = 3;

for i in range(100):
    tess.right(92)
    tess.forward(size)
    size += 3
