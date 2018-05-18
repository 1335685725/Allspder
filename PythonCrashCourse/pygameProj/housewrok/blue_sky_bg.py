import pygame
import sys


def show():
    pygame.init()
    screen = pygame.display.set_mode((800,610))
    bg_color = (9,22,218)
    pygame.display.set_caption("Blue Sky")
    while True:
        check_events()
        screen.fill(bg_color)
        pygame.display.flip()

def check_events():
    # 监视键盘和鼠标
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
show()