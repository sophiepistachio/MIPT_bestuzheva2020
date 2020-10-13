import turtle


def reading_coords(filename):
    f = open(filename, 'r')
    lines = f.readlines()  # lines - список, в котором элементы (line) - строки файла
    res = []
    coords_for_number = []  # координаты для цифири
    for line in lines:
        line = line.strip()  # убирает пробелы
        if len(line) == 1:  # если встретили номер цифири (не той, что рисуем, а следующей)
            wow = int(line)
            if wow != 0:
                res.append(list(coords_for_number))  # сбор коо-т для рисуемой цифири завершен
                coords_for_number = []  # коо-ты очищаются для следующей цифири
        else:  # если в строке файла коо-ты, то разрежем строку по пробелам, в коо-ты для цифири запишем числ. значения
            coords_for_number.append([int(x) for x in line.split()])
    return res  # в итоге выводятся коо-ты рисуемой цифири, когда встечается номер следующей (односимвольная строка)


def number(A, delta):  # А - индекс, записанный как список, delta - отступ вправо для написания в строку след. цифири
    delta2 = delta + 15
    turtle.penup()
    turtle.goto(A[0][0] + delta, A[0][1])  # к началу рисования цифири с учетом сдвига вправо для написания в строку
    turtle.pendown()
    for i in range(len(A) - 1):
        turtle.goto(A[i + 1][0] + delta, A[i + 1][1])  # бегает по координатам цифири и рисует ее
    return delta2  # возвращает сдвиг вправо для следующей цифири


turtle.shape('turtle')
turtle.speed(1)
S = reading_coords('turtlecoords.txt')  # наши координаты в виде списка из списков из списков
delta = 0
for i in range(6):
    number(S[i], delta)
    delta = number(S[i], delta)  # подставляем в дельту дельту2, чтобы новую цифирь рисовать справа от этой
