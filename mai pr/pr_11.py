from os import write

import pygame
from django.template.defaultfilters import center
from pygame.color import THECOLORS

pygame.init()
dis= pygame.display.set_mode((400,400))

float=pygame.font.SysFont(None,24)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            dis_over=True
            pygame.quit()
    number=1

    for x in range(10,350,55):
        pygame.draw.rect(dis, (240, 230, 140), (x, 10, 50, 50), 1)

        for y in range(10, 350, 55):
            pygame.draw.rect(dis, (240, 230, 140), (x, y, 50, 50), 1)
    # for a in range(20, 400, 55):
    #     pygame.draw.rect(dis, (173, 255, 47), (a, 20, 30, 30), 1)
    #     for s in range(20, 400, 55):
    #          pygame.draw.rect(dis, (173, 255, 47), (a, s, 30, 30), 1)
            text_surface = font.render(str(number), True, (255,255,255))
            text_rect=text_surface.get_rect(center=(x+25, y+25))
            dis.blit(text_surface, text_rect)
            number+=1
pygame.display.update()

quit()