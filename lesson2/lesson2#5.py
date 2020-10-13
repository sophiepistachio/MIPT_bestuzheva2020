import turtle

turtle.shape('turtle')
for i in range(1,11,1):
  turtle.pendown()
  turtle.forward(i*10)
  turtle.left(90)
  turtle.forward(i*10)
  turtle.left(90)
  turtle.forward(i*10)
  turtle.left(90)
  turtle.forward(i*10)
  turtle.penup()
  turtle.forward(5)
  turtle.right(90)
  turtle.forward(5)
  turtle.right(180)
