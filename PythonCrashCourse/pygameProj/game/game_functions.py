import pygame
import sys
from pygameProj.game import bullet
from pygameProj.game import alien
from time import sleep


def check_events(ship, ai_settings, stats, button, sb, aliens,screen, bullets):
    '''
    :param ship:
    :return:
    '''
    # 监视键盘和鼠标
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_butoon(ai_settings, screen, stats, button, sb, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_butoon(ai_settings, screen, stats, button, sb, ship, aliens, bullets, mouse_x, mouse_y):
    '''在玩家单机play按钮时触发事件'''
    button_checked = button.rect.collidepoint(mouse_x, mouse_y)
    if   button_checked and not stats.game_active :
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重新统计游戏信息
        stats.reset_stats()
        stats.game_active = True
        #重置记分牌图像
        sb.prep_high_score()
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


#响应按下按键
def check_keydown_events(event, ship, ai_settings, screen, bullets):
    '''
    :param event:
    :param ship:
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        frie_bullets(bullets, ai_settings, screen, ship)

#响应松开按键
def check_keyup_events(event, ship):
    '''
    :param event:
    :param ship:
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_screen(ai_settings, screen, stats, sb, ai_ship, aliens, bullets, button):
    '''
    :param ai_settings:
    :param screen:
    :param ai_ship:
    :return:
    '''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ai_ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    # 让绘制的屏幕可见
    if not stats.game_active:
        button.drwa_butoon()
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens):
    '''更新子弹位置'''
    #更新子弹位置
    bullets.update()

    # 删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''
    响应子弹和外星人的碰撞
    :param ai_settings:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    '''
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    # 删除已消失子弹
    if 0 == len(aliens):
        # 删除现有子弹并创建新的外星人
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level += 1
        sb.prep_level()
        creat_fleet(ai_settings, screen, ship, aliens)

def frie_bullets(bullets ,ai_settings, screen, ship):
    # 创建一颗子弹，并将其放入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    '''
    计算屏幕容纳多少行外星人
    :param ai_settings:
    :param ship_height:
    :param alien_height:
    :return:
    '''
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows



def get_number_aliens_x(ai_settings, alien_width):
    '''计算一行中可以容纳多少个外星人'''
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''
    创建一个外星人并将其放在当前行
    :param ai_settings:
    :param screen:
    :param aliens:
    :param alien_number:
    :return:
    '''
    ai_alien = alien.Alien(ai_settings, screen)
    alien_width = ai_alien.rect.width
    ai_alien.x = alien_width + 2 * alien_width * alien_number
    ai_alien.rect.x = ai_alien.x
    ai_alien.rect.y = ai_alien.rect.height + 2 * ai_alien.rect.height * row_number
    aliens.add(ai_alien)

def creat_fleet(ai_settings, screen, ship, aliens):
    '''
    创建外星人群
    :param ai_settings:
    :param screen:
    :param aliens:
    :return:
    '''
    #创建一个外星人
    ai_alien = alien.Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, ai_alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, ai_alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)




def check_fleet_edges(ai_settings, aliens):
    '''
    有外星人到达边缘时采取相应措施
    :param ai_settins:
    :param aliens:
    :return:
    '''
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break



def change_fleet_direction(ai_settings, aliens):
    '''
    将外星人整体下移并改变他们的方向
    :param ai_settings:
    :param aliens:
    :return:
    '''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    '''
    响应外星人与飞船碰撞
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    '''
    if stats.ships_left > 0:
        #将飞船数量-1
        stats.ships_left -= 1
        sb.prep_ships()
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人,并将飞船放置在屏幕底部中心
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #暂停
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, screen, aliens, ship, bullets, sb):
    '''
    更新所有外星人的设置s
    :param aliens:
    :return:
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    '''检查是否外星人到达底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom :
            #像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break

def check_high_score(stats, sb):
    '''检查是否有新的最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()