import turtle
import math
turtle.shape("turtle")
k=3
n=0
for i in range (3,13,1):
    turtle.left(90+180/i)
    turtle.forward(15+10*(i-2))
    for k in range (i-1):
        turtle.left(360/i)
        turtle.forward(15+10*(i-2))
    turtle.right(90-180/i)
    turtle.penup()
    turtle.forward(10*((i-2)+1)/(2*math.sin(math.pi/(i+1)))-10*(i-2)/(2*math.sin(math.pi/i)))
    turtle.pendown()
