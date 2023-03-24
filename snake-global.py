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
    s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((255,255,255,128))                         # notice the alpha value in the color
    fenetre.blit(s, (0,0))
    fenetre.blit(fond, (0, 0))
    for i in range (0, 350, 10):
        pygame.draw.rect(fenetre,(255,255,255),(0,i,0,0))
        for j in range (0, 1000, 10):
            pygame.draw.rect(fenetre,(255,255,255),(0,i,10,10))
    
    pygame.display.flip()
pygame.quit()
