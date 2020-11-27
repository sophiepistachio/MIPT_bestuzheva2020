import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 700))

maxx=800
maxy=700

#задаем цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

cdvig = [-3, -2, -1, 1, 2, 3]

score = 0

def new_ball():
    circle(screen, color, (x, y), r)




pygame.display.update()
clock = pygame.time.Clock()
finished = False
click = False

while not finished:
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    vx = cdvig[randint(0, 5)]
    vy = cdvig[randint(0, 5)]
    click = False
    while (finished == False) and (click == False):
        new_ball()
        x = x + vx
        y = y + vy
        #постоянная скорость цикла
        clock.tick(FPS)
        if x+r >= maxx or x-r <= 0:
            vx = vx * (-1)
        if y+r >= maxy or y-r <= 0:
            vy = vy * (-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                    score += 1
                    print('счет ', score)
                    click = True
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
