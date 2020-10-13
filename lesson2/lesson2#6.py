import turtle
n = int(input('Enter n'))
turtle.shape('turtle')
for i in range(1,n+1,1):
  turtle.forward(100)
  turtle.stamp()
  turtle.backward(100)
  turtle.left(360/n)
