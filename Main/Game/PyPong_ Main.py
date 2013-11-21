import pygame
from pygame.locals import *

import random
import sys
black = ( 0, 0, 0)
white = ( 255, 255, 255)
default_border_color= green = ( 0, 255, 0)
P1_scores = red = ( 255, 0, 0)
P2_scores = blue = ( 0, 0, 255)
Score_board = orange = (255, 127, 0)
pygame.init()

size = [700,600]
Surface = pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")

done = False

clock = pygame.time.Clock()

circle_x, circle_y = 350, 250
default_circle_x, default_circle_y = 350, 250
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

P1_border_color = None
P2_border_color = None
Top_border_color = None
Bottom_border_color = None

''' -------- Main Program Loop STARTS -------- '''
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
	''' GAME VARIABLES BEGIN '''
	P1_border_color = default_border_color
	P2_border_color = default_border_color
	Top_border_color = default_border_color
	Bottom_border_color = default_border_color
	''' GAME VARIABLES END '''
	''' GAME LOGIC STARTS '''
	''' BOUNCING THE BALL LOGIC STARTS '''
	if circle_y > 484 or circle_y < 16:
		circle_y_change *= -1
	''' BOUNCING THE BALL LOGIC ENDS '''
	''' BALL-RACQUET COLLISION TESTING STARTS '''
	if (circle_x==racquet1_x2) and (racquet1_y2<circle_y<racquet1_y1): 
		circle_x_change *= -1
	if (circle_x==racquet2_x2) and (racquet2_y1<circle_y<racquet2_y2):
		circle_x_change *= -1
	''' BALL-RACQUET COLLISION TESTING ENDS '''
	''' GAME LOGIC ENDS '''
	''' SCORING/SCOREBOARD LOGIC STARTS '''
	if circle_x > 684:
		P1_border_color = P2_scores
		circle_x_change *= -1
		circle_x, circle_y = default_circle_x, default_circle_y
	if circle_x < 16:
		P2_border_color = P1_scores
		circle_x_change *= -1
		circle_x, circle_y = default_circle_x, default_circle_y
	''' SCORING/SCOREBOARD LOGIC ENDS '''
	''' DRAW CODE STARTS '''
	''' PLAYERS AND BALLS '''
	Surface.fill(black)
	pygame.draw.circle(Surface,white,(circle_x,circle_y),4,0) #Ball
	pygame.draw.rect(Surface,red,[racquet1_x1,racquet1_y1,racquet1_width,racquet1_length]) #Player 1
	pygame.draw.rect(Surface,blue,[racquet2_x1,racquet2_y1,racquet2_width,racquet2_length]) #Player 2
	''' GAME ARENA'''
	pygame.draw.rect(Surface,P2_border_color,[0,0,10,699]) #Left Goal
	pygame.draw.rect(Surface,Bottom_border_color,[0,500,699,-10]) #Bottom
	pygame.draw.rect(Surface,P1_border_color,[700,500,-10,-699]) #Right Goal
	pygame.draw.rect(Surface,Top_border_color,[700,0,-699,10]) #Top
	''' SCOREBOARD DRAW CODE '''
	pygame.draw.rect(Surface,Score_board,[0,501,10,99]) #Left Barrier
	pygame.draw.rect(Surface,Score_board,[0,590,699,10]) #Bottom Barrier
	pygame.draw.rect(Surface,Score_board,[700,601,-10,-89]) #Right Barrier
	pygame.draw.rect(Surface,Score_board,[700,501,-699,10]) #Top Barrier
	pygame.draw.rect(Surface,Score_board,[340,510,10,99]) #Divider
	''' DRAW CODE ENDS '''
	''' SCREEN UPDATE STARTS '''
	pygame.display.flip()
	clock.tick(20)
	''' SCREEN UPDATE ENDS '''
	''' MISC CHANGES STARTS '''
	circle_x += circle_x_change 
	circle_y += circle_y_change
	racquet1_x2, racquet1_y2 = (racquet1_x1+racquet1_width), (racquet1_y1+racquet1_length)
	racquet2_x2, racquet2_y2 = (racquet2_x1+racquet2_width), (racquet2_y1+racquet2_length)
	''' MISC CHANGES END '''
''' -------- Main Program Loop Ends -------- '''
pygame.quit()