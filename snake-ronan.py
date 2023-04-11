# import pygame
# from pygame.locals import QUIT, RESIZABLE

# pygame.init()
# fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

# fond = pygame.image.load("./image/fond-lunaire.jpg").convert()
# continuer = 1
# while continuer:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             continuer = 0
#     fenetre.blit(fond, (0, 0))
#     pygame.draw.rect(fenetre,(0,0,0),(0,0,80,80))
#     pygame.draw.rect(fenetre,(255,255,255),(0,80,80,80))
#     pygame.display.flip()
# pygame.quit()

# importing pygame module

import pygame
import random
# importing sys module
import sys
 
# initialising pygame
pygame.init()
clock = pygame.time.Clock()

windowWidth = 640
windowHeight = 480
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
fenetre = pygame.display.set_mode((1000, 700))
fenetre.fill((white))
sprite = pygame.draw.rect(fenetre, red, (300,300,30,15))
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    fenetre.blit(mesg, [fenetre_width / 2, fenetre_height / 2])    

while not game_over:
        while game_close == True:
            fenetre.fill(white)
            message("R Retry or Q for Quit ", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
        
clock.tick(60)
pygame.display.update()
from tkinter import *
from timeit import default_timer

# Fenetre = Tk()
# def updateTime():
#     now = default_timer() - start
#     minutes,seconds = divmod(now, 60)
#     hours, minutes =  divmod(minutes, 60)
#     str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
#     canvas.itemconfigure(text_clock, text=str_time)
#     Fenetre.after(1000,updateTime)

# canvas = Canvas(Fenetre, width=800, height=800, bg="white")
# canvas.pack(padx=10,pady=10)

# start = default_timer()
# text_clock = canvas.create_text(40,20)
# updateTime()
# Fenetre.mainloop()