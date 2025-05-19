import pygame 
import sys 

def desenha_texto (texto, fonte, cor, superficie, x, y): 
    texto_obj = fonte.render (texto, True, cor)
    texto_rect = texto_obj.get_rect ()
    texto_rect.center = (x, y)
    superficie.blit (texto_obj, texto_rect)

def tela_de_creditos (tela, status): 
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)

    fonte_titulo = pygame.font.Font ("fontes/fonte1.ttf", 100)
    fonte_texto = pygame.font.Font ("fontes/fonte3.ttf", 26)

    tela.fill (88, 110, 124)
    mouse_x = pygame.mouse.get_pos()
    mouse_y = pygame.mouse.get_pos()

    