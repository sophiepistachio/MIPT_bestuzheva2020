from math import pi, sin, cos, inf
import turtle
turtle.shape('turtle')
for i in range (10000):
  t=i/100*pi
  dx=t*cos(t)
  dy=t*sin(t)
  turtle.goto(dx, dy)
