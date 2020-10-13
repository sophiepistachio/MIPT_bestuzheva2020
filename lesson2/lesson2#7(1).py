import turtle

n = int(input('Enter n '))
turtle.shape('turtle')
for i in range(n):
    turtle.forward(i*0.005)
    turtle.left(1)
    i += 1
    
