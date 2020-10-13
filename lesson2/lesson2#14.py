import turtle
import numpy as np

n = int(input('Введите нечетное число '))

turtle.shape('turtle')

for i in range (n):
    turtle.forward(200)
    turtle.left(180-180/n)
