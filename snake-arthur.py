import pygame
import random

# initialisation de pygame
pygame.init()

# définition des dimensions de l'écran
screen_width = 640
screen_height = 480

# définition des couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# définition de la taille des blocs
block_size = 10

# définition de la vitesse du serpent
clock = pygame.time.Clock()
snake_speed = 15

# définition de la police
font = pygame.font.SysFont(None, 25)

# fonction pour afficher le score
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width/6, screen_height/3])

# fonction pour afficher le serpent
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

# fonction pour exécuter le jeu
def gameLoop():
    game_over = False
    game_close = False

    # initialisation de la position du serpent
    lead_x = screen_width / 2
    lead_y = screen_height / 2

    # initialisation de la direction du serpent
    lead_x_change = 0
    lead_y_change = 0

    # initialisation de la liste du serpent
    snake_list = []
    snake_length = 1

    # initialisation de la position de la nourriture
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    while not game_over:

        # si le joueur a perdu, afficher un message et permettre de rejouer ou quitter le jeu
        while game_close == True:
            screen.fill(white)
            message_to_screen("Vous avez perdu! Appuyez sur Q pour quitter ou sur C pour rejouer", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # gérer les événements du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
        # empêcher le serpent de sortir de l'écran
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True
            
        # mettre à jour la position du serpent
        lead_x += lead_x_change
        lead_y += lead_y_change

        # effacer l'écran
        screen.fill(white)

        # dessiner la nourriture
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # mettre à jour la liste du serpent
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # détecter si le serpent a mangé la nourriture
        if lead_x == foodx and lead_y == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # détecter si le serpent a touché son corps
        for eachSegment in snake_list[:-1]:
            if eachSegment == snake_head:
                game_close = True

        # dessiner le serpent
        draw_snake(block_size, snake_list)

        # afficher le score
        message_to_screen("Score: " + str(snake_length - 1), black)

        # mettre à jour l'affichage
        pygame.display.update()

        # réguler la vitesse du serpent
        clock.tick(snake_speed)
gameLoop()
