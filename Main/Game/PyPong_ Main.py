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



racquet1_x1, racquet1_y1 = 680, 440
racquet1_x2, racquet1_y2 = None, None
racquet1_width = -10
racquet1_length = -40
racquet1_x_change, racquet1_y_change = 5, 5

racquet2_x1, racquet2_y1 = 20, 20
racquet2_x2, racquet2_y2 = None, None
racquet2_width = 10
racquet2_length = 40
racquet2_x_change, racquet2_y_change = 5, 5

border_color = green

''' -------- Main Program Loop Begins -------- '''
while done == False:
	''' EVENT PROCESSING STARTS '''
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop 
	keys_held = pygame.key.get_pressed()
	if keys_held[K_UP]:
		racquet1_y1 -= racquet1_y_change
	if keys_held[K_DOWN]:
		racquet1_y1 += racquet1_y_change
	if keys_held[ord('w')]:
		racquet2_y1 -= racquet2_y_change
	if keys_held[ord('s')]:
		racquet2_y1 += racquet2_y_change
	''' EVENT PROCESSING ENDS '''
	''' GAME LOGIC STARTS '''
	''' BOUNCING THE BALL LOGIC STARTS '''
	if circle_x > 684 or circle_x < 16:
		circle_x_change *= -1
	if circle_y > 484 or circle_y < 16:
		circle_y_change *= -1
	''' BOUNCING THE BALL LOGIC ENDS '''
	''' BALL-RACQUET COLLISION TESTING BEGINS '''
	if (circle_x==racquet1_x2) and (racquet1_y2<circle_y<racquet1_y1): 
		circle_x_change *= -1
	if (circle_x==racquet2_x2) and (racquet2_y1<circle_y<racquet2_y2):
		circle_x_change *= -1
	''' BALL-RACQUET COLLISION TESTING ENDS '''
	''' GAME LOGIC ENDS '''
	''' DRAW CODE STARTS'''
	Surface.fill(black)
	pygame.draw.circle(Surface,white,(circle_x,circle_y),4,0) #Ball
	pygame.draw.rect(Surface,red,[racquet1_x1,racquet1_y1,racquet1_width,racquet1_length]) #Player 1
	pygame.draw.rect(Surface,blue,[racquet2_x1,racquet2_y1,racquet2_width,racquet2_length]) #Player 2
	''' GAME ARENA DRAW CODE '''
	pygame.draw.rect(Surface,border_color,[0,0,10,700]) #Left Goal
	pygame.draw.rect(Surface,border_color,[0,500,700,-10]) #Bottom
	pygame.draw.rect(Surface,border_color,[700,500,-10,-700]) #Right Goal
	pygame.draw.rect(Surface,border_color,[700,0,-700,10]) #Top
	''' DRAW CODE ENDS '''
	''' SCREEN UPDATE STARTS '''
	pygame.display.flip()
	clock.tick(20)
	''' SCREEN UPDATE ENDS '''
	''' MISC CHANGES BEGIN'''
	circle_x += circle_x_change 
	circle_y += circle_y_change
	racquet1_x2, racquet1_y2 = (racquet1_x1+racquet1_width), (racquet1_y1+racquet1_length)
	racquet2_x2, racquet2_y2 = (racquet2_x1+racquet2_width), (racquet2_y1+racquet2_length)
	''' MISC CHANGES END '''
''' -------- Main Program Loop Ends -------- '''
pygame.quit()