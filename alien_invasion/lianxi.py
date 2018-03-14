import pygame

import random

SCREEN_RECT = pygame.Rect(0,0,480,600)
#创建敌机监听事件  敌机定时器
BULLET_HERO_EVENT = pygame.USEREVENT + 1

CREATE_EVENT = pygame.USEREVENT
class PlaneGame(pygame.sprite.Sprite):

	def __init__(self,new_image,speed=1):
		
		super().__init__()
		#初始化精灵 属性
		self.image = pygame.image.load(new_image)
		self.speed = speed
		#获取精灵位置
		self.rect = self.image.get_rect()

	def update(self):

		self.rect.y += self.speed

class BackGround(PlaneGame):

	def __init__(self,is_a = False):

		super().__init__("./Runoob/images/background.png")
		self.rect.top = 0
		if is_a :
			self.rect.bottom = self.rect.top  


	def update(self):

		super().update()

		if self.rect.y == SCREEN_RECT.height:
			self.rect.y = -self.rect.height 

class Enemy(PlaneGame):

	def __init__(self):
		super().__init__("./Runoob/images/enemy1.png")
		#设置初始化速度
		self.speed = random.randint(1,3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)


	def update(self):
		super().update()

		if self.rect.y == SCREEN_RECT.height:
			self.kill()

class Hero(PlaneGame):

	def __init__(self):
		super().__init__("./Runoob/images/life.png")
		#英雄飞机初始位置  中心轴一致
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom
		#创建子弹精灵组
		self.bullets = pygame.sprite.Group()

	def update(self):

		self.rect.x += self.speed
		
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
			self.rect.x = SCREEN_RECT.width - self.rect.width

	def fire(self):

		for i in range(1,4):
			#子弹位置初始化
			bullet = Bullet()
			bullet.rect.bottom = self.rect.y - 10 * i
			bullet.rect.centerx = self.rect.centerx
			#将精灵添加到精灵组
			self.bullets.add(bullet)



class Bullet(PlaneGame):

	def __init__(self):
		super().__init__("./Runoob/images/bullet2.png",-3)
		#self.speed = 3
	def update(self):
		super().update()
		#self.rect.y -= 2
		if self.rect.bottom <= SCREEN_RECT.y:
			self.kill()
