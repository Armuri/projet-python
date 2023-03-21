import pygame
from pygame.locals import QUIT, RESIZABLE

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
fond = pygame.image.load("./image/fond-lunaire.jpg").convert()
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    fenetre.blit(fond, (0, 0))

    pygame.display.flip()
cell_x = 10
cell_y = 10
 
column = 0
row = 0
 
while column < 3:
	while row < 3:
		print("Creation case au positions x:" + str(cell_x) + " y: " + str(cell_y))
		background.blit(cell, (cell_x, cell_y))
		cell_y += 100+10
		row += 1
		cell_x += 100+10
		column += 1

pygame.quit()