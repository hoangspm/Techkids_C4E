def draw_square(size):
    pendown()
    color("pink")
    for i in range(4):
        forward(size)
        left(90)


from turtle import *

bgcolor("lightgreen")
pensize(3)
speed(-1)

size = 20;
for i in range(20):
    draw_square(size)
    penup()
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(180)
    size += 20;
