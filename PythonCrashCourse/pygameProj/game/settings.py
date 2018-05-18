class Settings():
    '''存储《外星人》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30
        #外星人的速度
        self.fleet_drop_speed = 10
        #有多少艘飞船
        self.ship_limit = 3

        self.speed_scale = 1.1

        #计分
        self.alien_points = 50
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        # 飞船的速度
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction为1表示右移，-1为左移
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        print(self.alien_points)







