#!/usr/bin/env python2

import sys, pygame

pygame.init()

if True:
	pygame.mixer.init()
	pygame.mixer.music.load("music/battle.it")
	pygame.mixer.music.play(-1)

size = width, height = 320, 240
speed = [2, 2]
bgcolor = 255, 255, 255
framerate = 60

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball = pygame.image.load("sprites/zebra_ex.png")
ballrect = ball.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	
	screen.fill(bgcolor)
	screen.blit(ball, ballrect)
	pygame.display.flip()

	clock.tick(framerate)
