import pygame.image
from button import *


White = (255,255,255)
color = (161, 161, 161)
pygame.init()

opening_sound = pygame.mixer.Sound("open.mp3")
map_sound = pygame.mixer.Sound("map.mp3")

# 배경 이미지
background = pygame.image.load("img1/back.png")
tree_img = pygame.image.load("img1/tree.png")
sun_img = pygame.image.load("img1/sun.png")
sky_img = pygame.image.load("img1/sky.png")
# 제목
font = pygame.font.SysFont("cambria", 70)
title = font.render('Haemi wheat in the maze', True, color)

#버튼
button_surface = pygame.image.load("img1/button.png")
button_surface = pygame.transform.scale(button_surface, (150, 50))
start_button = Button(button_surface, 650, 425, "Start")
rule_button = Button(button_surface, 650, 500, "rule")
back_button = Button(button_surface, 650, 650, "back")
exit_button = Button(button_surface, 650, 575, "exit")



def opening_make():
    # 배경그리기
    screen.blit(sky_img, (0, -20))
    screen.blit(background, (0, 100))
    screen.blit(tree_img, (820, 100))
    screen.blit(sun_img, (0, 0))
    # 제목
    screen.blit(title, (300, 150))
    start_button.update()
    start_button.changeColor(pygame.mouse.get_pos())
    rule_button.update()
    rule_button.changeColor(pygame.mouse.get_pos())
    exit_button.update()
    exit_button.changeColor2(pygame.mouse.get_pos())
    pygame.display.update()

def rule_make():
    screen.fill("Black")
    img1 = pygame.image.load("img/key.png")
    img1 = pygame.transform.scale(img1, (200, 40))
    img2 = pygame.image.load("img/box.png")
    img2 = pygame.transform.scale(img2, (200, 150))
    img3 = pygame.image.load("img/exit.png")
    img3 = pygame.transform.scale(img3, (170, 50))
    font = pygame.font.SysFont("나눔바른고딕", 40)
    rule_text = font.render('- 조작키 설명.', True, White)
    rule_text2 = font.render('맵에서 움직일 수 있고'
                             '점프를 할 수 있습니다.', True, White)
    rule_text3 = font.render('문제를 풀 수 있습니다.', True, White)
    rule_text4 = font.render('탈출할 수 있습니다.', True, White)
    screen.blit(rule_text, (300, 50))
    screen.blit(rule_text2, (450, 150))
    screen.blit(rule_text3, (450, 300))
    screen.blit(rule_text4, (450, 450))
    back_button.update()
    back_button.changeColor(pygame.mouse.get_pos())
    screen.blit(img1, (200, 150))
    screen.blit(img2, (200, 250))
    screen.blit(img3, (200, 450))
    pygame.display.update()