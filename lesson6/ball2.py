import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
#создание экрана и счета
screen = pygame.display.set_mode((700, 700))
f = open('score1.txt', 'w')
f = open('score1.txt', 'r')

#цвета шариков
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global x, y, r
#новый шарик
def new_ball():
    global x, y, r
    x = randint(10, 800)
    y = randint(10, 700)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    dx = 2
    dy = 2
    # while True:
    # # смена позиции
    #     x += dx
    #     y += dy
    # # проверка границ
    #     if x - dx < 0 or x + dx > 700:
    #         dx = -dx
    #     if y - dy < 0 or y + dy > 700:
    #         dy = -dy


pygame.display.update()
clock = pygame.time.Clock()
finished = False

Score = []
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            def click():
                print(x, y, r)
            def coords():
                for event in pygame.event.get():
                    print(event.pos[0], event.pos[1])
            def great():
                if (((x - event.pos[0])**2) + ((y - event.pos[1])**2) + r**2) < 2 * r ** 2:
                    print('Great')
                    Score.append(1)
                    print('счёт:', len(Score))
                else:
                    print('haha')
            for line in f:
                print('игрок1:', len(Score))

            click()
            coords()
            great()






    new_ball()
    pygame.display.update()
    screen.fill(BLACK)


f.close()
pygame.quit()
