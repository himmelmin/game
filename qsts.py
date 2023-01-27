import random

import pygame
from button import Button

White = (250, 250, 250)

pygame.init()
screen_height = 700  # 세로 크기
screen_width = 1280  # 가로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Questions!")
a = [
     ["print를 사용하는 것들 중 맞지 않는 것은?","23", "1-2", "'hollow'","'hollow"],
     ["다음중 데이터 형 변환이 아닌 것은?", "str", "int", "float", "if"],
     ["몫만 계산해주는 연산자는 무엇인가요?", "%", "**", "&", "//"],
     ["라이브러리를 호출하는 명령어는 무엇인가요?", "if", "while", "from", "import"],
     ["다음중 반복문으로 사용할 수 없는 함수는 무엇인가?", "for", "for else", "While", "if"]
     ]

font = pygame.font.SysFont("나눔바른고딕", 40)
button_surface = pygame.image.load("img1/button.png").convert_alpha()
button_surface = pygame.transform.scale(button_surface, (150, 50))

# 랜덤 문제를 출력한다.
i = random.randint(0,4)
a = a[i]
aq = a[0]
a1 = a[1]
a2 = a[2]
a3 = a[3]
a4 = a[4]
qst_text1 = font.render(aq, True, White)
right1_button = Button(button_surface, 650, 425, a1)
right2_button = Button(button_surface, 650, 500, a2)
right3_button = Button(button_surface, 650, 575, a3)
wrong_button = Button(button_surface, 650, 650, a4)


def qsts1():
    run = True
    while run:
        screen.fill("black")
        screen.blit(qst_text1, (200, 250))
        right1_button.update()
        right2_button.update()
        right3_button.update()
        wrong_button.update()
        right1_button.changeColor(pygame.mouse.get_pos())
        right2_button.changeColor(pygame.mouse.get_pos())
        right3_button.changeColor(pygame.mouse.get_pos())
        wrong_button.changeColor(pygame.mouse.get_pos())
        pygame.display.update()
        if right1_button.draw(screen) or right2_button.draw(screen) or right3_button.draw(screen):
            return "no"
        elif wrong_button.draw(screen):
            return "yes"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False