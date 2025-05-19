import pygame
import random

# Definir algumas coisas do PyGame
pygame.init ()
COMP_TELA = 900
ALTURA_TELA = 600
tela = pygame.display.set_mode (COMP_TELA, ALTURA_TELA)
pygame.display.set_caption('Jogo de DesSoft')
relogio = pygame.time.Clock()
correr = True

dt = 0 
pos_jogador = pygame.Vector2(tela.get_width()/2, tela.get_height())