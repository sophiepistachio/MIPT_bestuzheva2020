import turtle
import random

n = int(input('Введите число '))
a = int(input('Введите промежуток '))
b = int(input())

turtle.shape('turtle')
turtle.speed(10)
for i in range (n):
  x = random.randint(a, b)
  y = random.randint(1, 360)
  z = random.randint(1, 360)
  turtle.forward(x)
  turtle.left(y)
  turtle.right(z)
