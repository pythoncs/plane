import pygame

from lianxi import *

# 初始化
pygame.init()
# 加载
pygame.mixer.music.load("./Runoob/东京热.mp3")
# 播放
pygame.mixer.music.play()


class PlanGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        self.clock = pygame.time.Clock()

        self.__creat_sprites()
        pygame.time.set_timer(CREATE_EVENT, 1000)
        pygame.time.set_timer(BULLET_HERO_EVENT, 200)

    def start_game(self):
        # 开始游戏
        while True:
            # 设置帧率
            self.clock.tick(60)
            # 监听事件
            self.__handler_event()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵 精灵组
            self.__update_sprites()
            # 更新窗口
            pygame.display.update()

    def __creat_sprites(self):
        # 创建精灵 精灵组
        png1 = BackGround()
        png2 = BackGround(True)

        self.back_group = pygame.sprite.Group(png1, png2)

        self.enemy2 = Enemy()
        self.enemy_group = pygame.sprite.Group(self.enemy2)

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __handler_event(self):
        # 监听事件
        for event in pygame.event.get():
            print(event)
            my_pressed = pygame.key.get_pressed()

            if my_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif my_pressed[pygame.K_LEFT]:
                self.hero.speed = -2

            else:
                self.hero.speed = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == CREATE_EVENT:
                self.enemy_group.add(Enemy())
                print(self.enemy_group)
            elif event.type == BULLET_HERO_EVENT:
                self.hero.fire()



    def __check_collide(self):
        # 碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        if len(enemies) > 0:
        	self.hero.kill()

        	pygame.quit()
        	exit()

    def __update_sprites(self):
        # 更新精灵 精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)


        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


if __name__ == "__main__":

    game = PlanGame()

    game.start_game()

