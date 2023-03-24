import pygame
from pygame.locals import QUIT, RESIZABLE

pygame.init()
fenetre = pygame.display.set_mode((1000, 650), RESIZABLE)
screen = pygame.display.get_surface()
pygame.display.set_caption( 'Blue Snake') #titre de la fenetre

fond = pygame.image.load("./image/fond-lunaire.jpg").convert()
continuer = 1

police = pygame.font.SysFont("Montserrat", 70)
police1 = pygame.font.SysFont("Montserrat", 30)
image_texte = police.render ("Blue Snake",2 , (45,85,255))
image_texte1 = police1.render ("Score : 0",2 , (0,0,0))

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    s = pygame.Surface((1000,1000), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((255,255,255,255))                         # notice the alpha value in the color
    fenetre.blit(s, (0,0))
    fenetre.blit(fond, (100,800))
    screen.blit(image_texte, (375,10,10,10))
    screen.blit(image_texte1, (30,20,10,10))
    # si l'utilisateur presse n'importe quel touche de direction, le snake gagne +1 (haut,bas,gauche,droite) et perd 1 de longeur
    for i in range(10, 30, 10): 
        pygame.draw.rect(fenetre,(45,85,255),(120,450,i,12))
    
    
    pygame.display.flip()
pygame.quit()
