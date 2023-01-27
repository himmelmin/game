import pygame
# 게임 화면 크기 설정
def map_size():
    screen_width = 1300  # 가로 크기
    screen_height = 720  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("game!")