import pygame

#初始化方法
pygame.init()

#创建游戏屏幕宽和高          
screen = pygame.display.set_mode((480,600))
#游戏循环
while True:
	pass
	#加载图片
	bg = pygame.image.load("./Runoob/images/background.png")
	#绘制到屏幕上
	screen.blit(bg,(0,0))
	#刷新屏幕
	#pygame.display.update()

	#创建英雄
	hero = pygame.image.load("./Runoob/images/life.png")
	#绘制到屏幕上
	screen.blit(hero,())
	#刷新屏幕         更新
	pygame.display.update()
		   #显示	


#退出
pygame.quit()