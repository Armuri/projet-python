import pygame
<<<<<<< Updated upstream
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
#affichage de la fenêtre
fen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Chrono")
fpsClock = pygame.time.Clock()
 
<<<<<<< Updated upstream
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

=======
from pygame.locals import*
 
pygame.init()
  
#affichage de la fenêtre
fen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Chrono")
fpsClock = pygame.time.Clock()
 
=======
>>>>>>> Stashed changes
TpsZero = pygame.time.get_ticks() ## Départ
def temps():
    seconds = (pygame.time.get_ticks() - TpsZero) / 1000
    print(seconds)
     
continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
        if evenement.type == KEYDOWN:
            if evenement.key == K_ESCAPE:
                continuer = False
                 
    temps()
     
    pygame.display.flip()
    fpsClock.tick(60)
<<<<<<< Updated upstream
 
>>>>>>> Stashed changes
pygame.quit()
=======
    
    pygame.quit()
>>>>>>> Stashed changes
