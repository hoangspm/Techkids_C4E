#turtle_2_fill_color
from turtle import *
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

n = 5

for i in range(n):
    color(colors[i])
    begin_fill()
    
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    
    end_fill()
    forward(50)
