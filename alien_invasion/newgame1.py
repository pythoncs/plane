import pygame

from screen_rect import *


class PlaneGame(object):

    def __init__(self):

        # 创建窗口初始化
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵 精灵组
        self.__create_sprites()
        # 定时器（每秒创建一个敌机）
        pygame.time.set_timer(CREATE_ENEMY, 1000)

    def start_game(self):
        # 开始游戏
        while True:
            # 设置刷新帧率
            self.clock.tick(60)
            # 监听事件
            self.__handler_event()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵 精灵组（绘制）
            self.__update_sprites()
            # 刷新屏幕
            pygame.display.update()

    def __create_sprites(self):

        # 创建精灵 精灵组
        png1 = BackGround()
        png2 = BackGround()
        png2.rect.y = -png2.rect.height
        self.back_group = pygame.sprite.Group(png1, png2)

        enemy2 = Enemy()
        self.enemy_group = pygame.sprite.Group()

    def __handler_event(self):
        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == CREATE_ENEMY:
                self.enemy_group.add(Enemy())

    def __check_collide(self):
        # 碰撞检测
        pass

    def __update_sprites(self):
            # 更新精灵 精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)


if __name__ == "__main__":
    game = PlaneGame()

    game.start_game()
