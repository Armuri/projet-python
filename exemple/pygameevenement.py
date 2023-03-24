#initialisation
import pygame
from pygame.locals import *
pygame.init()

#construction de la fenetre
fenetre = pygame.display.set_mode( (640,480) ) #taille en pixels : 640x480
pygame.display.set_caption('Jolie fenetre') #titre de la fenetre

#code de jeu a completer
#...

#definition des images
balle = pygame.image.load("https://www.angelique-renaud.com/pygame/balle3.png").convert_alpha()
fond = pygame.image.load("https://www.angelique-renaud.com/pygame/background.jpg").convert()

continuer = 1

while continuer == 1 :
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = 0
        #autres evenements
        
    #positionnement des images
    fenetre.blit(fond, (0,0))
    fenetre.blit(balle, (320,240))
    #affichage
    pygame.display.flip()

pygame.quit()