import turtle
import numpy as np

m = int(input())
turtle.shape('turtle')
turtle.left(90)
def circle (n, r):
    for i in range(n):
        turtle.forward(2*np.pi*r/n)
        turtle.left(360/n)

for i in range (m):
        circle(70,50+i*10)
        turtle.left(180)
        circle(70,50+i*10)
        turtle.left(180)
