
import pygame 
import sys 

def desenha_texto (texto, fonte, cor, superficie, x, y): 
    texto_obj = fonte.render (texto, True, cor)
    texto_rect = texto_obj.get_rect() 
    texto_rect.center = (x, y)
    superficie.blit (texto_obj, texto_rect)

def tela_inicial (comprimento, altura, tela, status): 
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    AZUL = (4, 124, 252)
    AMARELO = (249, 194, 60)
    VERMELHO = (237, 53, 91)

    fonte_titulo = pygame.font.Font ("fontes/fonte1.ttf", 130)
    fonte_texto = pygame.font.Font ("fontes/fonte3.ttf", 26)
