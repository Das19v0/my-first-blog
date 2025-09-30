import math

import pygame
from pygame.colordict import THECOLORS
from sqlparse.utils import offset

pygame.init()
dis= pygame.display.set_mode((500,500))


dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            dis_over=True
    dis.fill((95, 158, 160))

    r=pygame.Rect(150,300,200,200)
    color=(255, 255, 255)
    pygame.draw.ellipse(dis,color,r)

    r = pygame.Rect(170, 200, 160, 160)
    color = (255, 255, 255)
    pygame.draw.ellipse(dis, color, r)

    r = pygame.Rect(190, 120, 120, 120)
    color = (255, 255, 255)
    pygame.draw.ellipse(dis, color, r)

    pygame.draw.circle(dis,(0,0,0),(230,160), 5)
    pygame.draw.circle(dis, (0, 0, 0), (270, 160), 5)
    pygame.draw.polygon(dis,(255, 99, 71), [(250,170),(290,180),(250,190)])

    scarf_color=(139, 0, 139)
    pygame.draw.rect(dis,scarf_color,(180,210,130,20))
    pygame.draw.rect(dis,scarf_color,(200,220,20,50))

    pygame.draw.circle(dis, (0, 0, 0), (250, 200), 2)
    pygame.draw.circle(dis, (0, 0, 0), (245, 198), 2)

    pygame.draw.circle(dis, (0, 0, 0), (250, 270), 6)
    pygame.draw.circle(dis, (0, 0, 0), (250, 290), 6)
    pygame.draw.circle(dis, (0, 0, 0), (250, 360), 6)
    pygame.draw.circle(dis, (0, 0, 0), (250, 390), 6)

    pygame.draw.line(dis,(80,40,0),(175,250), (100,190), 8)
    pygame.draw.line(dis, (80, 40, 0), (325, 250), (405, 180), 8)

    pygame.draw.polygon(dis,(47, 79, 79), [(165,150),(330,150),(280,70),(220,70)])
    pygame.draw.polygon(dis, (0,0,0),[(165,150),(330,150),(280,70),(220,70)],3)

    font=pygame.font.SysFont("Arial",48)
    bold=True
    text=font.render("Снеговик", True, (255,255,255))
    dis.blit(text,(170,10))

    pygame.display.update()
quit()