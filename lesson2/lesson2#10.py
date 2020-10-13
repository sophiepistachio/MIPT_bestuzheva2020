import turtle
import numpy as np


def circle (n, r):
    for i in range(n):
        turtle.forward(2*np.pi*r/n)
        turtle.left(360/n)


for i in range (6):
    turtle.left(60)
    circle (50,50)
