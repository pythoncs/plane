import pygame

screen = pygame.display.set_mode((480,622))

png = pygame.image.load("./Runoob/images/background.png")

screen.blit(png,(0,0))

hero = pygame.image.load("./Runoob/images/life.png")

screen.blit(hero,(217,565))

hero_rect = pygame.Rect(217,565,46,57)

clock = pygame.time.Clock()

pygame.init()

while True:

	#hero_rect -= 1

	clock.tick(60)

	screen.blit(png,(0,0))
	screen.blit(hero,hero_rect)

	pygame.display.update()


	for event in pygame.event.get():
		print(event)
		a = True
		if event.type == pygame.KEYDOWN:
			
			if a:

				if event.key == 27:
					pygame.quit()
					exit()
				#向上	
				elif event.key == 273:
					hero_rect.y -= 5
				#向下
				elif event.key == 274:
					hero_rect.y += 5
				#向右
				elif event.key == 275:
					hero_rect.x += 5
				#向左
				elif event.key == 276:
					hero_rect.x -= 5










pygame.quit()