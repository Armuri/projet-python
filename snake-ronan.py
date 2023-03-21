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
    pygame.draw.rect(fenetre,(0,0,0),(0,0,80,80))
    pygame.draw.rect(fenetre,(255,255,255),(0,80,80,80))
    pygame.display.flip()
pygame.quit()