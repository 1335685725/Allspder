import pygame
from pygameProj.game import settings
from pygameProj.game import ship
from pygameProj.game import game_functions as gf
from pygame.sprite import Group
from pygameProj.game import game_stats
from pygameProj.game import button
from pygameProj.game import scoreboard
from pygameProj.game import alien

def run_game():
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一个game_stats对象用于统计游戏信息
    play_button = button.Button(ai_settings, screen, "Play")
    stats = game_stats.GameStats(ai_settings)
    sb = scoreboard.Scoreboard(ai_settings, screen, stats)
    #创建一艘飞船
    ai_ship = ship.Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.creat_fleet(ai_settings, screen, ai_ship, aliens)

    #开始游戏主循环s
    while True:
        gf.check_events(ai_ship, ai_settings, stats, play_button, sb, aliens, screen, bullets)

        if stats.game_active:
            ai_ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ai_ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats,  screen, aliens, ai_ship, bullets, sb)
        gf.update_screen(ai_settings, screen, stats, sb, ai_ship, aliens, bullets, play_button)

run_game()







