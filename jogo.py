
import pygame
import random

#setup do Pygame 
pygame.init()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Teste3')
clock = pygame.time.Clock()
running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)