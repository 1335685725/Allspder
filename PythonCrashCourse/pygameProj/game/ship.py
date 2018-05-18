import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        #初始化飞船并设置其初始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load(r'C:\Python\pygameProj\game\ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将每艘新飞船放在屏幕的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #将飞船的坐标放进去
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center_x+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 0:
            self.center_x-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.center_y+=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.centery > 0:
            self.center_y-=self.ai_settings.ship_speed_factor

        #根据self.center_x和self.center_y更新飞船坐标
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        # self.center = self.screen_rect.centerx
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom

