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
JAUNE = (255, 255, 0)



# Définition de la taille de la fenêtre
TAILLE_ECRAN = (1500, 750)
ecran = pygame.display.set_mode(TAILLE_ECRAN)

# Définition de la police d'écriture
police = pygame.font.SysFont(None, 25)

# Définition de la vitesse du serpent
VITESSE = 25

# Définition de la taille de la grille
TAILLE_CASE = 25
NB_COLONNES = TAILLE_ECRAN[0] // TAILLE_CASE
NB_LIGNES = TAILLE_ECRAN[1] // TAILLE_CASE


# Définition des directions possibles
HAUT = 0
BAS = 1
GAUCHE = 2
DROITE = 3

temps = 0
endtime = 0

# Définition de la fonction pour dessiner la grille
def dessiner_grille():
    for x in range(0, TAILLE_ECRAN[0], TAILLE_CASE):
        pygame.draw.line(ecran, BLANC, (x,0), (x,TAILLE_ECRAN[1]))
    for y in range(0, TAILLE_ECRAN[1], TAILLE_CASE):
        pygame.draw.line(ecran, BLANC, (0,y), (TAILLE_ECRAN[0],y))

# Définition de la fonction pour dessiner le serpent
def dessiner_serpent(corps):
    for pos in corps:
        pygame.draw.rect(ecran, VERT, [pos[0], pos[1], TAILLE_CASE, TAILLE_CASE])

# Définition de la fonction pour dessiner la pomme
def dessiner_pomme(position):
    pygame.draw.rect(ecran, JAUNE, [position[0], position[1], TAILLE_CASE, TAILLE_CASE])

# Définition de la fonction pour afficher le score
def afficher_score(score):
    texte = police.render("Score: " + str(score), True, BLANC)
    ecran.blit(texte, [0, 0])

# Fonction pour afficher le temps

# Fonction pour afficher l'écran de fin de jeu
def ecran_game_over(score, temps_actuel):
    # Effacer l'écran
    ecran.fill(NOIR)

    # Afficher le texte de fin de jeu
    font_grand = pygame.font.SysFont(None, 40)
    texte_score = font_grand.render("Score final: " + str(score), True, BLANC)
    texte_temps = font_grand.render("Temps écoulé: " + str(temps_actuel) + " secondes", True, BLANC)
    texte_rejouer = font_grand.render("Appuyez sur 'ESPACE' pour rejouer", True, BLANC)
    texte_quitter = font_grand.render("Appuyez sur 'Q' pour quitter", True, BLANC)
    ecran.blit(texte_score, (TAILLE_ECRAN[0]/2 - texte_score.get_width()/2, TAILLE_ECRAN[1]/2 - texte_score.get_height() - 50))
    ecran.blit(texte_temps, (TAILLE_ECRAN[0]/2 - texte_temps.get_width()/2, TAILLE_ECRAN[1]/2))
    ecran.blit(texte_rejouer, (TAILLE_ECRAN[0]/2 - texte_rejouer.get_width()/2, TAILLE_ECRAN[1]/2 + texte_rejouer.get_height() + 50))
    ecran.blit(texte_quitter, (TAILLE_ECRAN[0]/2 - texte_rejouer.get_width()/2, TAILLE_ECRAN[1]/2 + texte_quitter.get_height() + 90))

    # Mettre à jour l'affichage
    pygame.display.flip()

     # Attendre que le joueur appuie sur la touche 'ESPACE' ou 'Q'
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    attente = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    SystemExit
    
    # Redémarrer le jeu
    jeu()



# Définition de la fonction principale
def jeu():
    # Initialisation du jeu
    pygame.init()
    ecran = pygame.display.set_mode(TAILLE_ECRAN)
    pygame.display.set_caption("The Cosmic Snake")
    

    #image de fond
    fond = pygame.image.load("Rimae_Sirsalis.jpg")
    fond = pygame.transform.scale(fond, TAILLE_ECRAN)

    # Initialisation du serpent et de la pomme
    serpent = [[TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE*2],
   [TAILLE_ECRAN[0]//2, TAILLE_ECRAN[1]//2 + TAILLE_CASE*3]]
    direction = GAUCHE
    
    temps = pygame.time.get_ticks()
        
    # Fonction pour finir le jeu
    def fin_jeu():
        # Calcul du temps écoulé depuis le début du jeu
        temps_actuel = pygame.time.get_ticks()
        

        # Afficher l'écran de fin de jeu
        endtime = str((temps_actuel - temps)/ 1000);
        ecran_game_over(score, endtime)
        
    def afficher_temps(ecran):
        temps_actuel = pygame.time.get_ticks()
        font = pygame.font.SysFont(None, 30)
        texte = font.render("Temps: " + str((temps_actuel - temps)/ 1000) + "s", True, BLANC) 
        ecran.blit(texte, (10, TAILLE_ECRAN[1] - 30))
    
    # Fonction pour générer une nouvelle pomme
    
    def generer_pomme1(serpent):
        pomme1 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
    
        # Vérification que la pomme 1 n'apparaît pas sur le corps du serpent
        while pomme1 in serpent:
            pomme1 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
        return pomme1
    pomme1 = generer_pomme1(serpent)
    
    # Fonction pour générer une deuxième pomme
    
    def generer_pomme2(serpent):
        pomme2 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
    
        # Vérification que la pomme 2 n'apparaît pas sur le corps du serpent
        while pomme2 in serpent:
            pomme2 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
        return pomme2
    pomme2 = generer_pomme2(serpent)
    
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
        afficher_temps(ecran)

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
           fin_jeu()
           

        # Gestion de la collision avec le corps
        if serpent[0] in serpent[1:]:
            fin_jeu()
            

        # Gestion de la collision avec la pomme 1 et 2
        VITESSE = 25
        if serpent[0] == pomme1:
            pomme1 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
            score += 10
            VITESSE = VITESSE + 20
        elif serpent[0] == pomme2:
            pomme2 = [random.randint(0, NB_COLONNES-1)*TAILLE_CASE, random.randint(0, NB_LIGNES-1)*TAILLE_CASE]
            score += 10
            VITESSE = VITESSE + 20
        else:
            serpent.pop()
    

        # Affichage des éléments
        ecran.blit(fond, (0, 0))
        #dessiner_grille()
        dessiner_serpent(serpent)
        dessiner_pomme(pomme1)
        dessiner_pomme(pomme2)
        afficher_score(score)
        afficher_temps(ecran)
        pygame.display.update()

        # Attente avant de mettre à jour l'écran
        pygame.time.wait(1000//VITESSE)


# Lancement du jeu
jeu()
