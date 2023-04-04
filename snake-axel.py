import pygame
import random


# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
AZUR = (0, 127, 255)
GRIS = (96,96,96)

#taille fenêtre game over
taille = largeur, hauteur = 800, 600

# Définition de la taille de la fenêtre
TAILLE_ECRAN = (800, 600)
ecran = pygame.display.set_mode(TAILLE_ECRAN)

# Définition de la police d'écriture
police = pygame.font.SysFont(None, 25)

# Définition de la vitesse du serpent
VITESSE = 10
#VITESSE = 20
#VITESSE = 30

# Définition de la taille de la grille
TAILLE_CASE = 25
NB_COLONNES = TAILLE_ECRAN[0] // TAILLE_CASE
NB_LIGNES = TAILLE_ECRAN[1] // TAILLE_CASE

# Déclaration de la constante temps
TEMPS_DEBUT = pygame.time.get_ticks()  # Temps écoulé depuis le début du jeu

# Fonction pour afficher le temps
def afficher_temps():
    temps_actuel = pygame.time.get_ticks() - TEMPS_DEBUT
    font = pygame.font.SysFont(None, 30)
    texte = font.render("Temps: " + str(temps_actuel // 1000) + "s", True, BLANC)
    ecran.blit(texte, (10, TAILLE_ECRAN[1] - 30))


# Définition des directions possibles
HAUT = 0
BAS = 1
GAUCHE = 2
DROITE = 3

# Définition de la fonction pour dessiner la grille
def dessiner_grille():
    for x in range(0, TAILLE_ECRAN[0], TAILLE_CASE):
        pygame.draw.line(ecran, BLANC, (x,0), (x,TAILLE_ECRAN[1]))
    for y in range(0, TAILLE_ECRAN[1], TAILLE_CASE):
        pygame.draw.line(ecran, BLANC, (0,y), (TAILLE_ECRAN[0],y))

# Définition de la fonction pour dessiner le serpent
def dessiner_serpent(corps):
    for pos in corps:
        pygame.draw.rect(ecran, AZUR, [pos[0], pos[1], TAILLE_CASE, TAILLE_CASE])

# Définition de la fonction pour dessiner la pomme
def dessiner_pomme(position):
    pygame.draw.rect(ecran, ROUGE, [position[0], position[1], TAILLE_CASE, TAILLE_CASE])

# Définition de la fonction pour afficher le score
def afficher_score(score):
    texte = police.render("Score: " + str(score), True, BLANC)
    ecran.blit(texte, [0, 0])

# Fonction pour afficher le temps
def afficher_temps(ecran):
    temps_actuel = pygame.time.get_ticks() - TEMPS_DEBUT
    font = pygame.font.SysFont(None, 30)
    texte = font.render("Temps: " + str(temps_actuel // 1000) + "s", True, BLANC)
    ecran.blit(texte, (10, TAILLE_ECRAN[1] - 30))

def game_over():
    """Fonction permettant d'afficher l'écran de Game Over"""
    #Le fond
    ecran.fill(GRIS)
    #Les rectangles
    rect_again = pygame.draw.rect(ecran,ROUGE, [largeur-(largeur*0.85), hauteur-(hauteur*0.33), largeur/3.2, hauteur/10])
    rect_quit = pygame.draw.rect(ecran, ROUGE, [largeur-(largeur*0.15+largeur/3.5), hauteur-(hauteur*0.33), largeur/3.2, hauteur/10])
    contour_a = pygame.draw.rect(ecran, NOIR, [largeur-largeur*0.85, hauteur-hauteur*0.33, largeur/3.2, hauteur/10], 2)
    contour_q = pygame.draw.rect(ecran, NOIR, [largeur-(largeur*0.15+largeur/3.5), hauteur-(hauteur*0.33), largeur/3.2, hauteur/10], 2)
    #La police
    pol_go = pygame.font.SysFont("Perpetua Titling MT", 130)
    pol_buttons = pygame.font.SysFont("Perpetua Titling MT", 40)
    #Les textes
    txt_go = pol_go.render("GAME OVER", True, BLANC)
    txt_again = pol_buttons.render("AGAIN", True, NOIR)
    txt_quit = pol_buttons.render("QUIT", True, NOIR)
    #Les positions
    pos_go = txt_go.get_rect()
    pos_again = txt_again.get_rect()
    pos_quit = txt_quit.get_rect()
    pos_go.centerx = ecran.get_rect().centerx
    pos_again.centerx = largeur-largeur*0.7
    pos_quit.centerx = largeur-(largeur*0.15+largeur/3.5) + largeur*0.16
    pos_go.centery = hauteur*0.3
    pos_again.centery = hauteur-(hauteur*0.28)
    pos_quit.centery = pos_again.centery
    #On colle sur la fenêtre
    ecran.blit(txt_go, pos_go)
    ecran.blit(txt_again, pos_again)
    ecran.blit(txt_quit, pos_quit)


# Définition de la fonction principale
def jeu():
    # Initialisation du jeu
    pygame.init()
    ecran = pygame.display.set_mode(TAILLE_ECRAN)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    #image de fond
    fond = pygame.image.load("Rimae_Sirsalis.jpg")
    fond = pygame.transform.scale(fond, TAILLE_ECRAN)

    # Initialisation du serpent et de la pomme
    serpent = [[TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE*2],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE*3],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE*4]]
    direction = DROITE
    # Fonction pour générer une nouvelle pomme

    def generer_pomme(serpent):
        pomme = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
    
        # Vérification que la pomme n'apparaît pas sur le corps du serpent
        while pomme in serpent:
            pomme = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
        return pomme
    pomme = generer_pomme(serpent)
    score = 0
    
    # Boucle de jeu
    while True:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != BAS:
                    direction = HAUT
                elif event.key == pygame.K_DOWN and direction != BAS:
                    direction = BAS
                elif event.key == pygame.K_LEFT and direction != DROITE:
                    direction = GAUCHE
                elif event.key == pygame.K_RIGHT and direction != GAUCHE:
                    direction = DROITE

         # Calcul du temps écoulé
        temps_actuel = pygame.time.get_ticks() - TEMPS_DEBUT

        # Déplacement du serpent
        nouvelle_tete = [serpent[0][0], serpent[0][1]]
        if direction == HAUT:
            nouvelle_tete[1] -= TAILLE_CASE
        elif direction == BAS:
            nouvelle_tete[1] += TAILLE_CASE
        elif direction == GAUCHE:
            nouvelle_tete[0] -= TAILLE_CASE
        elif direction == DROITE:
            nouvelle_tete[0] += TAILLE_CASE

        serpent.insert(0, nouvelle_tete)
        
        # Gestion de la collision avec les bords
        if serpent[0][0] < 0 or serpent[0][0] >= TAILLE_ECRAN[0] or serpent[0][1] < 0 or serpent[0][1] >= TAILLE_ECRAN[1]:
           pygame.quit()
           quit()


        # Gestion de la collision avec le corps
        if serpent[0] in serpent[1:]:
            pygame.quit()
            quit()

        # Gestion de la collision avec la pomme
        if serpent[0] == pomme:
            pomme = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
            score += 10
        else:
            serpent.pop()

        # Affichage des éléments
        ecran.blit(fond, (0, 0))
        #dessiner_grille()
        dessiner_serpent(serpent)
        dessiner_pomme(pomme)
        afficher_score(score)
        afficher_temps(ecran)
        pygame.display.update()

        # Attente avant de mettre à jour l'écran
        pygame.time.wait(1000//VITESSE)

        

# Lancement du jeu
jeu()


