import turtle
import numpy as np

m = int(input())
turtle.shape('turtle')
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.left(90)
def hcircle (n, r):
    for i in range(n//2):
        turtle.forward(2*np.pi*r/n)
        turtle.left(360/n)
for i in range (m):
    hcircle (100,50)
    hcircle(50,10)
