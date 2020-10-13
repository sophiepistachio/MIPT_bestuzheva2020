import turtle


def number(A, delta):  # M - индекс, записанный как список, delta - отступ вправо для написания в строку след. цифири
    delta2 = delta + 15
    turtle.penup()
    turtle.goto(A[0][0] + delta, A[0][1])  # к началу рисования цифири с учетом сдвига вправо для написания в строку
    turtle.pendown()
    for i in range(len(A) - 1):
        turtle.goto(A[i + 1][0] + delta, A[i + 1][1])  # бегает по координатам цифири и рисует ее
    return delta2  # возвращает сдвиг вправо для следующей цифири


x = 0
y = 0
coords = [(x, y), (x + 10, y), (x, y - 10), (x + 10, y - 10), (x, y - 20), (x + 10, y - 20)]
one = [coords[2], coords[1], coords[5]]
two = [coords[0],coords[1],coords[3],coords[4],coords[5]]
three = [coords[0],coords[1],coords[2],coords[3],coords[4]]
four = [coords[0], coords[2], coords[3], coords[5], coords[1]]
five = [coords[1],coords[0],coords[2],coords[3],coords[5],coords[4]]
six = [coords[1],coords[2],coords[4],coords[5],coords[3],coords[2]]
seven = [coords[0], coords[1], coords[2], coords[4]]
eight = [coords[0],coords[4],coords[5],coords[1],coords[0],coords[2],coords[3]]
nine = [coords[4],coords[3],coords[1],coords[0],coords[2],coords[3]]
zero = [coords[0], coords[1], coords[5], coords[4], coords[0]]


delta = 0
S = [0] * 6
M = [0] * 6
for i in range(6):
    S[i] = int(input())

for i in range(6):
    if S[i]==1:
        M[i]=one
    elif S[i]==2:
        M[i]=two
    elif S[i]==3:
        M[i]=three
    elif S[i]==4:
        M[i]=four
    elif S[i]==5:
        M[i]=five
    elif S[i]==6:
        M[i]=six
    elif S[i]==7:
        M[i]=seven
    elif S[i]==8:
        M[i]=eight
    elif S[i]==9:
        M[i]=nine
    else:
        M[i]=zero
turtle.shape('turtle')
for i in range(6):
    number(M[i], delta)
    delta = number(M[i], delta)  # подставляем в дельту дельту2, чтобы новую цифирь рисовать справа от этой
turtle.ht()
turtle.mainloop()

def coords_to_file():  # подготовим файл для следующего упражнения
    f = open("turtlecoords.txt", 'w')
    res = ""  # в переменную запишем особым образом координаты, а потом переменную запишем в файл
    for i in range(len(M)):
        res += str(i) + "\n"  # с новой строки записываем номер рисуемой цифири
        for coord in M[i]:  # M[i] - список из кортежей coord, которые в свою очередь состоят из пары х и у
            res += str(coord[0]) + " " + str(coord[1]) + "\n"  # с новой строки записываем х и у через пробел
    res += '6'  # для корректного выполнения следующего упражнения
    f.write(res)
    f.close()

coords_to_file()
