#turtle_1
from turtle import *
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

n = 7

for i in range(3,n+1):
    color(colors[i-3])
    for j in range(i):
        forward(100)
        left(360/i)
