# # # data=["Tom", 37, "Google"]
# # # tom=tuple(data)
# # # print(tom)
# # #
# # # tom= ("Tom", 37,"Google", "software developer")
# # # print(tom[0])
# # # print(tom[1])
# # # print(tom[-1])
# # #
# # myfile=open("hello.txt", "w")
# # myfile.close()
# #
# # try:
# #     myfile=open("hello.txt", "w")
# #     try:
# #         print("Рaбота с файлом")
# #     finally:
# #         myfile.close()
# # except Exception as ex:
# #     print(ex)
# #
# with open("hello.txt", "w") as myfile:
#     print("Работа с файлом myfile")
#
# with open("hello.txt", "w") as file:
#     file.write("Hello Python")
# print("Файл записан")
#
# with open("hello.txt", "a") as file:
#     file.write("\nhello work")
# print("Файл изменен")
#
import pygame
from pygame import Surface
from pygame.draw import lines
#
# lines=["Hello Word\n", "Hello Work\n", "Hello World\n"]
# with open("hello.txt", "a") as file:
#     file.writelines(lines)
# print("Список строк записан в файл")
#
# with open("hello.txt", "a") as my
#
# import pygame
#
# pygame.init()
# dis= pygame.display.set_mode((500,400))
#
# pygame.display.update()
#
# pygame.quit()
# quit()

import pygame

pygame.init()
dis= pygame.display.set_mode((500,400))


dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(event)
            pygame.quit()
    r=pygame.Rect(150,100,200,200)
    color=(240, 230, 140)
    pygame.draw.rect(dis, color,r,0)
    r = pygame.Rect(240, 120, 80, 80)
    color = (255,165,0)
    pygame.draw.rect(dis, color,(),0)
    r = pygame.Rect(200, 220, 100, 80)
    color = (139, 0, 0)
    pygame.draw.rect(dis, color, r, 0)
    pygame.display.update()
quit()