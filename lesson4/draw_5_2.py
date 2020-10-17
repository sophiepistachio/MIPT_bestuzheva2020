import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1000, 720))

#рисуем фон
polygon(screen, (254, 214, 163), [(0,0), (1000,0), (1000,180), (0,180)])
polygon(screen, (254, 214, 197), [(0,180), (1000,180), (1000,360), (0,360)])
polygon(screen, (254, 214, 149), [(0,360), (1000,360), (1000,510), (0,510)])
#polygon(screen, (192, 143, 143), [(0,510), (1000,510), (1000,720), (0,720)])
circle(screen, (255, 240, 0), (500, 150), 60) #солнце
#оранжевая гора
polygon(screen, (255, 140, 0), [(0,360), (1000,240), (915,205), (865,220),(800,185), (755, 200),(700,135),(665,135),(630,170), (595,210), (525,230), (500,260),(450,240),(400,310),(365,295),(290,305), (170,210),(155,180), (115,165), (15,285),(0,330)])
circle(screen, (255, 140, 0), (680, 143), 17) #изгиб горы
#кирпичная гора
polygon(screen,(173, 65, 49), [(0,540),(1000,490),(1000,275),(960,345),(910,340),(885,380),(835,345),(785,410),(685,360),(565,360),(505,425),(410,440),(340,375),(250,360),(220,450),(150,410),(110,490),(10,380),(0,370)])
#изгибы горы
circle(screen, (173, 65, 49), (625, 400), 71)
ellipse(screen, (173, 65, 49), (10,300,130,520))
#оставшаяся часть фона
polygon(screen, (180, 135, 149), [(0,540), (1000,490), (1000,720), (0,720)])
#темная гора
polygon(screen, (44, 7, 33), [(0,720),(1000,720),(1000,470),(970,490),(940,520),(835,600),(765,630),(740,635),(715,630),(645,600),(480,680),(390,665),(360,645),(245,510),(150,440),(0,410)])
#разные чаечки
polygon(screen,(64, 27, 3),[(250,240),(230,228),(232,226),(238,227),(245,230),(251,235),(253,232),(262,228),(272,227)])
polygon(screen,(64, 27, 3),[(330,260),(310,248),(312,246),(318,247),(325,250),(331,255),(333,252),(342,248),(352,247)])
polygon(screen,(64, 27, 3),[(430,240),(410,228),(412,226),(418,227),(425,230),(431,235),(433,232),(442,228),(452,227)])
polygon(screen,(64, 27, 3),[(350,300),(330,288),(332,286),(338,287),(345,290),(351,295),(353,292),(362,288),(372,287)])
polygon(screen,(64, 27, 3),[(390,270),(370,258),(372,256),(378,257),(385,260),(391,265),(393,262),(402,258),(412,257)])
polygon(screen,(64, 27, 3),[(790,520),(770,508),(772,506),(778,507),(785,510),(791,515),(793,512),(802,508),(812,507)])
polygon(screen,(64, 27, 3),[(690,550),(670,538),(672,536),(678,537),(685,540),(691,545),(693,542),(702,538),(712,537)])
polygon(screen,(64, 27, 3),[(780,590),(750,570),(745,564),(746,562),(755,563),(765,567),(782,580),(785,574),(800,564),(820,558)])
polygon(screen,(64, 27, 3),[(610,500),(580,480),(575,474),(576,472),(585,473),(595,477),(612,490),(615,484),(630,474),(650,468)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
