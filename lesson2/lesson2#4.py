import turtle
import numpy as np

n=360
r=50

turtle.shape('turtle')
for i in range(n):
    turtle.forward(2*np.pi*r/n)
    turtle.left(360/n)
