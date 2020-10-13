from random import randint
from random import random
import turtle

number_of_turtles = 20
steps_of_time_number = 500
turtle.mode("logo")  # для удобства ориентирую на север

turtle.ht()
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(-200, 200)
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)  # рисую стенки сосуда

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-195, 195), randint(-195, 195))
    unit.right(360 * random())
    unit.shapesize(0.6, 0.6, 0.6)  # расселяю молекулы по сосуду

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(1)
        for i in range(number_of_turtles):
            if abs(pool[i].xcor() + 200) <= 5 or abs(pool[i].xcor() - 200) <= 5:
                pool[i].seth(-pool[i].heading())
                pool[i].forward(1)  # молекулы не выходят за вертикальные стенки

            if abs(pool[i].ycor() + 200) <= 5 or abs(pool[i].ycor() - 200) <= 5:
                pool[i].seth(pool[i].heading() - 180)
                pool[i].forward(1)  # молекулы не выходят за горизонтальные стенки

            for j in range(number_of_turtles):
                if i != j and abs(pool[i].xcor() - pool[j].xcor()) <= 5 and abs(pool[i].ycor() - pool[j].ycor()) <= 5:
                    k = pool[i].heading()
                    pool[i].setheading(pool[j].heading())
                    pool[j].setheading(k)
                    pool[i].forward(1)
                    pool[j].forward(1)
# мол-лы равной массы, бегают с одинак. скоростью, потому центральный удар обменивает их направлениями скоростей
# мол-лы здесь - мат. точки, взаимодейтсвующие друг с другом и со стенками посредством абсолютно упругих соударений
