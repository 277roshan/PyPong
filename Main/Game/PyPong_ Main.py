import pygame
from pygame.locals import *

import random
import sys
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)
blue = ( 0, 0, 255)
pygame.init()

size = [700,500]
Surface = pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")

done = False

clock = pygame.time.Clock()
circle_x, circle_y = 350, 250
circle_x_change, circle_y_change = 5, 5

racquet1_x, racquet1_y = 670, 440
racquet1_x_change, racquet1_y_change = 5, 5

racquet2_x, racquet2_y = 20, 20
racquet2_x_change, racquet2_y_change = 5, 5

racquet_width = 12
racquet_length = 40

''' -------- Main Program Loop Begins -------- '''
while done == False:
	''' EVENT PROCESSING STARTS '''
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
		if event.type == KEYDOWN:
			if event.key == K_UP:
				racquet1_y -= racquet1_y_change
			if event.key == K_DOWN:
				racquet1_y += racquet1_y_change
			if event.key == ord('w'):
				racquet2_y -= racquet2_y_change
			if event.key == ord('s'):
				racquet2_y += racquet2_y_change
	''' EVENT PROCESSING ENDS '''
	''' GAME LOGIC STARTS '''
	''' BOUNCING THE BALL LOGIC STARTS '''
	if circle_x == 695 or circle_x < 0:
		circle_x_change *= -1
	if circle_y > 495 or circle_y < 0:
		circle_y_change *= -1
	''' BOUNCING THE BALL LOGIC ENDS '''
	''' BALL-RACQUET COLLISION TESTING BEGINS '''
	if (20<=circle_x<=32) and (20<circle_y==60):
		circle_x_change *= -1
		circle_y_change *= -1
	if (670<=circle_x<=692) and (440<=circle_y<=480):
		circle_y_change = (circle_y_change * -1)
	''' BALL-RACQUET COLLISION TESTING ENDS '''
	''' GAME LOGIC ENDS '''
	''' DRAW CODE STARTS'''
	Surface.fill(black)
	pygame.draw.circle(Surface, white, (circle_x, circle_y), 4, 0) 
	pygame.draw.rect(Surface, red,[racquet1_x, racquet1_y, racquet_width, racquet_length])
	pygame.draw.rect(Surface, blue,[racquet2_x, racquet2_y, racquet_width, racquet_length])

	''' DRAW CODE ENDS '''
	''' SCREEN UPDATE STARTS '''
	pygame.display.flip()
	clock.tick(20)
	''' SCREEN UPDATE ENDS '''
	''' MISC CHANGES BEGIN'''
	circle_x += circle_x_change 
	circle_y += circle_y_change
	''' MISC CHANGES END '''
''' -------- Main Program Loop Ends -------- '''
pygame.quit()