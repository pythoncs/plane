import pygame

import random

SCREEN_RECT = pygame.Rect(0,0,480,622)

#创建敌机
CREATE_ENEMY = pygame.USEREVENT

class PlaneGame(pygame.sprite.Sprite):


	def __init__(self,new_image,speed=1):
		#精灵图片 速度 

		super().__init__()
		self.image = pygame.image.load(new_image)

		
		#获取精灵图片的位置
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):

		#默认背景图片垂直向下移动
		self.rect.y += self.speed

class BackGround(PlaneGame):

	def __init__(self):
		super().__init__("./Runoob/images/background.png")

	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			#self.rect.bottom = self.rect.top
			self.rect.y = -self.rect.height

class Enemy(PlaneGame):
	#图片 速度
	def __init__(self):
		super().__init__("./Runoob/images/enemy1.png",)
		#设置敌机初始随机速度
		self.speed = random.randint(2,4)
		#设置敌机的初始位置
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			self.kill()