def draw_square(size):
    pendown()
    color("pink")
    for i in range(4):
        forward(size)
        left(90)


from turtle import *
bgcolor("lightgreen")
pensize(3)

for i in range(20):
    draw_square(10)
    penup()
    forward(20)
