import pygame
import random
from  math import sqrt


FPS = 30
time = 0
score = 0

#задаем цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#вводим имя
name = input('Enter user`s name')


def table_top(i):
    return int(i[1])

#функция вывода имени в файле
def record_table(name, score):
    f = open('records.txt', 'a')
    f.write(name + ' ' + str(score) + '\n')
    f.close()

#сортировка
def sort_table():
    f = open('records.txt', 'r')
    results = []
    while True:
        res = f.readline()
        if res == '':
            break
        results.append(res)

    for i in range(len(results)):
        results[i] = results[i].split()

    f.close()
    fw = open('records.txt', 'w')
    results.sort(key=table_top, reverse=True)
    for i in range(len(results)):
        fw.write(str(results[i][0]) + " " + str(results[i][1]) + "\n")
    fw.close()

#создание движущихся шариков(функция)
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        r = random.randint(20, 100)
        self.image = pygame.Surface((r, r))
        self.image.set_colorkey(BLACK)
        self.rad = r//2
        color = COLORS[random.randint(0, 5)]
        self.circle = pygame.draw.circle(self.image, color, (r//2, r//2), r//2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 700), random.randint(100, 500))
        self.speedx = random.randint(5, 10)
        self.speedy = random.randint(-10, 10)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 800:
            self.speedx = random.randint(-10, 1)
        if self.rect.left < 0:
            self.speedx = random.randint(1, 10)
        if self.rect.bottom > 650:
            self.speedy = random.randint(-10, -1)
        if self.rect.top < 0:
            self.speedy = random.randint(1, 10)

#создание движущихся квадратиков(функция)
class Square(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        r = random.randint(20, 80)
        self.width = r
        self.image = pygame.Surface((r, r))
        self.image.set_colorkey(BLACK)
        color = COLORS[random.randint(0, 5)]
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 700), random.randint(100, 500))
        self.speedx = random.randint(5, 15)
        self.speedy = random.randint(-15, 15)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 800:
            self.speedx = random.randint(-15, 1)
        if self.rect.left < 0:
            self.speedx = random.randint(1, 15)
        if self.rect.bottom > 650:
            self.speedy = random.randint(-15, -1)
        if self.rect.top < 0:
            self.speedy = random.randint(1, 15)

pygame.init()
pygame.mixer.init()
#создаем экран
screen = pygame.display.set_mode((800,650))
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
squares = pygame.sprite.Group()
ball = Ball()
balls.add(ball)
all_sprites.add(ball)


running = True
while running:
    #постоянная скорость цикла
    clock.tick(FPS)
    if time > 600:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #обрабатываем щелчок мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #вычисляем попадание для круга и квадрата
            for sprite in balls:
                if sqrt((sprite.rect.center[0] - pos[0])**2 + (pos[1] - sprite.rect.center[1])**2) < sprite.rad:
                    sprite.kill()
                    score += 1

            for sprite in squares:
                if sprite.rect.right > pos[0] > sprite.rect.x and sprite.rect.bottom > pos[1] > sprite.rect.y:
                    sprite.kill()
                    score += 3
    #при окончании игры изменяем таблицу
    if running == False:
        record_table(name, score)
        sort_table()


#счетчик времени, добавление объектов
    time += 1
    if time%40 == 0:
        ball = Ball()
        balls.add(ball)
        all_sprites.add(ball)
    elif time%50 == 0:
        sq = Square()
        squares.add(sq)
        all_sprites.add(sq)
    all_sprites.update()

#обновление экрана
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
