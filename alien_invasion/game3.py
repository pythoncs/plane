import pygame

pygame.init()
#创建屏幕大小
screen = pygame.display.set_mode((480,622))
#调用背景图片
png = pygame.image.load("./Runoob/images/background.png")
#绘制背景图片
screen.blit(png,(0,0))
#调用英雄图片
hero = pygame.image.load("./Runoob/images/life.png")
#初始化英雄飞机坐标
hero_rect = pygame.Rect(217,565,46,57)
#绘制
screen.blit(hero,(217,565))
#创建时钟对象
clock = pygame.time.Clock()
while True:
	#设置帧数
	clock.tick(500)
	
	#英雄飞机图层往上移动
	hero_rect.y -= 10
	
	if hero_rect.bottom <= 0:
		hero_rect.y = 622

	#绘制	
	screen.blit(png,(0,0))
	screen.blit(hero,(hero_rect.x,hero_rect.y))
	#刷新屏幕
	pygame.display.update()

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()







pygame.quit()